#!/usr/bin/env python3
"""
CopperBuilds SERP Visibility Report Generator
Usage: python generate_report.py --trade hvac --city phoenix --state az [--domain example.com]
Outputs: copperbuilds/reports/[trade]-seo-report-[city]-[state]-[year]/index.html
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / "copperbuilds.env")

DFS_USER = os.getenv("DATAFORSEO_USERNAME")
DFS_PASS = os.getenv("DATAFORSEO_PASSWORD")

# ── Cache Config ──────────────────────────────────────────────────────────────

CACHE_DIR = Path(__file__).parent / "reports" / "_cache"
CACHE_TTL_DAYS = 30


def _cache_key(keyword: str, location: str) -> str:
    slug = f"{keyword}--{location}".lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return slug[:120]


def _load_cache(keyword: str, location: str) -> dict | None:
    path = CACHE_DIR / f"{_cache_key(keyword, location)}.json"
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        saved_at = datetime.fromisoformat(data["_cached_at"])
        if datetime.now() - saved_at > timedelta(days=CACHE_TTL_DAYS):
            return None  # stale — will refetch
        return data["result"]
    except Exception:
        return None


def _save_cache(keyword: str, location: str, result: dict) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = CACHE_DIR / f"{_cache_key(keyword, location)}.json"
    payload = {"_cached_at": datetime.now().isoformat(), "result": result}
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

# ── Trade Keyword Templates ───────────────────────────────────────────────────

# SERP keywords: 15 per trade — used for Map Pack analysis (1 API credit each).
TRADE_SERP_KEYWORDS = {
    "hvac": [
        "AC repair", "HVAC company", "air conditioning repair", "furnace repair",
        "HVAC contractor", "emergency HVAC", "air conditioning installation",
        "heating and cooling", "HVAC service", "central air repair",
        "AC installation", "heat pump repair", "HVAC maintenance",
        "air conditioner service", "heating repair",
    ],
    "plumbing": [
        "plumber", "emergency plumber", "plumbing company", "drain cleaning",
        "water heater repair", "pipe repair", "leak repair", "plumbing service",
        "water heater installation", "sewer line repair", "toilet repair",
        "faucet repair", "plumbing contractor", "clogged drain", "water heater replacement",
    ],
    "roofing": [
        "roofing company", "roof repair", "roof replacement", "roofer",
        "storm damage roof repair", "roofing contractor", "roof inspection",
        "shingle replacement", "flat roof repair", "roofing service", "emergency roof repair",
        "gutter installation", "roof leak repair", "new roof installation", "roofing estimate",
    ],
    "electrical": [
        "electrician", "electrical contractor", "electrical repair", "panel upgrade",
        "electrical service", "emergency electrician", "electrical installation",
        "outlet repair", "circuit breaker repair", "generator installation",
        "EV charger installation", "electrical inspection", "wiring repair",
        "lighting installation", "electrical company",
    ],
    "landscaping": [
        "landscaping company", "lawn care service", "lawn mowing service",
        "landscape design", "tree trimming", "lawn maintenance",
        "irrigation installation", "sod installation", "landscaper",
        "yard cleanup", "mulching service", "weed control service",
        "sprinkler repair", "landscape contractor", "lawn treatment",
    ],
    "painting": [
        "painting contractor", "house painter", "interior painting",
        "exterior painting", "painting company", "commercial painting",
        "residential painting", "cabinet painting", "painting service",
        "deck staining", "fence painting", "drywall repair and painting",
        "painting estimate", "painting crew", "painting professionals",
    ],
    "cleaning": [
        "house cleaning service", "maid service", "cleaning company",
        "deep cleaning service", "move out cleaning", "commercial cleaning",
        "office cleaning", "janitorial service", "residential cleaning",
        "cleaning professionals", "cleaning crew", "weekly cleaning service",
        "post construction cleaning", "carpet cleaning", "window cleaning",
    ],
    "concrete": [
        "concrete contractor", "concrete company", "driveway replacement",
        "concrete repair", "concrete driveway", "patio installation",
        "concrete patio", "sidewalk repair", "concrete resurfacing",
        "stamped concrete", "foundation repair", "concrete leveling",
        "garage floor coating", "concrete work", "decorative concrete",
    ],
    "pool": [
        "pool service", "pool cleaning service", "pool repair", "pool company",
        "pool installation", "pool maintenance", "swimming pool repair",
        "pool contractor", "pool resurfacing", "pool equipment repair",
        "pool opening service", "pool closing service", "pool inspection",
        "above ground pool installation", "inground pool builder",
    ],
    "general_contractor": [
        "general contractor", "home remodeling", "kitchen remodel",
        "bathroom remodel", "home renovation", "contractor",
        "remodeling company", "home improvement contractor", "room addition",
        "basement finishing", "deck building contractor", "home repair",
        "renovation contractor", "construction company", "remodeling contractor",
    ],
}

# Volume keywords: top 3 trades only — used for the DataForSEO volume batch call
# (flat rate up to 1,000 keywords). At fetch time the code pads to 1,000 by pulling
# from the other two trades, so the primary trade's keywords always fill first.
TRADE_VOLUME_KEYWORDS = {
    "hvac": [
        "AC repair", "HVAC company", "air conditioning repair", "furnace repair",
        "HVAC contractor", "emergency HVAC", "air conditioning installation",
        "heating and cooling", "HVAC service", "central air repair", "AC installation",
        "heat pump repair", "HVAC maintenance", "air conditioner service", "heating repair",
        "HVAC repair", "air conditioner repair", "AC unit repair", "heater repair",
        "ductwork repair", "air handler repair", "condenser repair", "evaporator coil repair",
        "compressor repair", "blower motor repair", "thermostat repair",
        "capacitor replacement", "fan motor repair", "contactor replacement", "duct repair",
        "AC compressor repair", "heat pump compressor repair", "refrigerant line repair",
        "furnace installation", "heat pump installation", "mini split installation",
        "central air installation", "ductless AC installation", "AC replacement",
        "furnace replacement", "HVAC replacement", "heat pump replacement", "new AC unit",
        "new HVAC system", "new furnace", "air conditioning replacement",
        "ductless mini split installation", "mini split system installation",
        "ductless heat pump installation", "packaged unit installation",
        "split system installation", "whole house AC installation", "AC maintenance",
        "AC tune-up", "furnace tune-up", "AC inspection", "furnace inspection",
        "HVAC inspection", "duct cleaning", "HVAC cleaning", "annual AC service",
        "spring AC service", "fall furnace service", "HVAC seasonal maintenance",
        "pre-season HVAC", "HVAC checkup", "AC filter replacement", "air filter service",
        "furnace filter replacement", "HVAC service contract", "HVAC maintenance plan",
        "preventive HVAC maintenance", "AC tune up cost", "emergency AC repair",
        "24 hour HVAC", "after hours AC repair", "emergency heating repair",
        "same day AC repair", "urgent HVAC service", "emergency air conditioning",
        "24 hour AC repair", "weekend HVAC repair", "emergency furnace repair",
        "HVAC emergency service", "24 hour furnace repair", "night HVAC service",
        "AC not cooling", "AC blowing warm air", "AC not working", "furnace not working",
        "furnace not turning on", "no heat in house", "house not cooling", "AC making noise",
        "AC leaking water", "AC freezing up", "AC tripping breaker", "HVAC not working",
        "heater not working", "AC won't turn on", "furnace won't start",
        "AC running but not cooling", "AC short cycling", "furnace blowing cold air",
        "no hot air from vents", "water dripping from AC", "uneven cooling",
        "high energy bill HVAC", "AC compressor not working", "thermostat not working",
        "thermostat blank screen", "no airflow from vents", "AC icing up",
        "frozen AC outside unit", "AC smells musty", "burning smell from AC",
        "AC rattling noise", "AC clicking noise", "heat pump not heating",
        "heat pump blowing cold air", "furnace keeps shutting off", "furnace short cycling",
        "hot and cold spots house", "AC blows hot air", "mini split", "ductless mini split",
        "ductless AC", "heat pump", "central air conditioning", "split system AC",
        "packaged unit", "gas furnace", "electric furnace", "boiler repair", "radiant heating",
        "window AC installation", "geothermal HVAC", "air handler unit", "variable speed AC",
        "two-stage furnace", "dual fuel heat pump", "multi-zone mini split",
        "ceiling cassette mini split", "concealed duct mini split", "rooftop unit",
        "RTU repair", "Carrier AC", "Carrier HVAC", "Lennox HVAC", "Trane AC", "Trane HVAC",
        "Rheem HVAC", "Goodman AC", "York HVAC", "American Standard HVAC", "Daikin mini split",
        "Bryant HVAC", "Ruud HVAC", "Mitsubishi mini split", "LG mini split", "Bosch HVAC",
        "Heil HVAC", "Armstrong furnace", "Amana HVAC", "MrCool mini split",
        "Pioneer mini split", "Carrier furnace repair", "Lennox furnace repair",
        "Trane HVAC repair", "Rheem AC repair", "Goodman furnace repair", "HVAC cost",
        "AC replacement cost", "furnace replacement cost", "HVAC repair cost",
        "AC repair cost", "AC unit cost", "new HVAC system cost", "HVAC installation cost",
        "furnace cost", "heat pump cost", "mini split cost", "AC maintenance cost",
        "HVAC estimate", "free HVAC estimate", "average HVAC replacement cost",
        "AC tune-up cost", "furnace inspection cost", "HVAC service call cost",
        "heat pump installation cost", "duct cleaning cost", "AC compressor replacement cost",
        "HVAC financing", "AC financing", "HVAC payment plan", "HVAC near me",
        "AC repair near me", "air conditioning repair near me", "furnace repair near me",
        "HVAC company near me", "AC company near me", "heating repair near me",
        "cooling company near me", "HVAC contractor near me", "furnace installation near me",
        "AC tune-up near me", "HVAC maintenance near me", "furnace service near me",
        "heat pump repair near me", "ductless AC near me", "mini split near me",
        "HVAC inspection near me", "AC installation near me", "24 hour AC repair near me",
        "emergency HVAC near me", "indoor air quality", "air purifier installation",
        "air filtration system", "UV air purifier", "whole home humidifier",
        "dehumidifier installation", "air scrubber installation", "HEPA filtration",
        "allergen air filter", "air quality testing", "whole house air purifier",
        "ERV installation", "HRV installation", "energy recovery ventilator",
        "whole house fan installation", "ventilation system installation",
        "smart thermostat installation", "Nest thermostat installation", "Ecobee installation",
        "programmable thermostat", "energy efficient HVAC", "high efficiency furnace",
        "SEER rating", "ENERGY STAR HVAC", "variable speed HVAC", "HVAC energy savings",
        "commercial HVAC", "commercial air conditioning", "commercial heating", "office HVAC",
        "commercial HVAC service", "building HVAC", "commercial HVAC repair",
        "commercial AC installation", "restaurant HVAC", "retail HVAC", "warehouse HVAC",
        "how long does AC last", "when to replace AC unit", "how often to service AC",
        "AC vs heat pump", "heat pump vs furnace", "mini split vs central air",
        "best HVAC system", "most reliable HVAC brand", "how to choose HVAC system",
        "how to lower AC bill", "refrigerant recharge", "Freon recharge", "R22 refrigerant",
        "R410A refrigerant", "refrigerant leak", "compressor replacement",
        "drain line cleaning", "condensate drain cleaning", "duct sealing", "duct insulation",
        "zoning system HVAC", "heat exchanger repair", "igniter replacement",
        "flame sensor replacement", "pressure switch HVAC", "expansion tank HVAC",
        "duct replacement", "air duct replacement", "NATE certified HVAC",
        "licensed HVAC technician", "best HVAC company", "top rated HVAC",
        "honest HVAC company", "reliable HVAC contractor", "certified HVAC",
        "residential HVAC service", "home AC repair", "Carrier Infinity series", "Trane XR15",
        "Lennox XC21", "Rheem Prestige series", "Goodman GSXC", "York YXV", "Daikin DX20VC",
        "Bryant Evolution", "Ruud Ultra series", "AC keeps running", "AC won't turn off",
        "heat pump reversing valve", "defrost cycle heat pump", "heat pump stuck in cooling",
        "AC tripping breaker repeatedly", "HVAC breaker keeps tripping",
        "furnace ignitor not working", "pilot light keeps going out",
        "furnace making banging noise", "AC makes noise when starting", "AC drain pan full",
        "AC drain clogged", "HVAC tax credit", "energy efficient tax credit HVAC",
        "HVAC rebate", "AC rebate", "furnace rebate", "utility rebate HVAC",
        "home energy audit", "HVAC energy audit", "energy star rebate",
        "VRF system installation", "VRF system repair", "chiller repair",
        "cooling tower repair", "data center HVAC", "server room cooling", "hydronic heating",
        "steam boiler repair", "hot water boiler repair", "chilled water system",
        "VAV box repair", "damper repair", "economizer repair", "commercial rooftop unit",
        "commercial package unit", "HVAC permit", "HVAC permit cost", "HVAC inspection permit",
        "EPA 608 certified", "NATE certified technician", "mold testing HVAC",
        "duct disinfection", "air duct mold removal", "asbestos duct removal",
        "carbon monoxide testing", "Carrier AC repair", "Carrier heat pump repair",
        "Carrier AC installation", "Carrier HVAC service", "Carrier AC not cooling",
        "Lennox AC repair", "Lennox heat pump repair", "Lennox AC installation",
        "Lennox HVAC service", "Trane AC repair", "Trane furnace repair",
        "Trane heat pump repair", "Trane AC installation", "Trane HVAC service",
        "Rheem furnace repair", "Rheem heat pump repair", "Goodman AC repair",
        "Goodman HVAC repair", "York AC repair", "York furnace repair",
        "York heat pump repair", "American Standard AC repair",
        "American Standard furnace repair", "Bryant AC repair", "Bryant furnace repair",
        "Ruud AC repair", "Ruud furnace repair", "Daikin mini split repair",
        "Daikin AC repair", "Mitsubishi mini split repair", "Mitsubishi ductless repair",
        "LG mini split repair", "Bosch heat pump repair", "1.5 ton AC", "2 ton AC",
        "2.5 ton AC", "3 ton AC", "3.5 ton AC", "4 ton AC", "5 ton AC", "80000 BTU furnace",
        "100000 BTU furnace", "120000 BTU furnace", "12000 BTU mini split",
        "18000 BTU mini split", "24000 BTU mini split", "36000 BTU mini split", "14 SEER AC",
        "16 SEER AC", "18 SEER AC", "20 SEER AC", "80 AFUE furnace", "90 AFUE furnace",
        "96 AFUE furnace", "98 AFUE furnace", "high efficiency heat pump", "SEER2 rating",
        "HSPF heat pump", "HVAC zoning system", "multi-zone HVAC", "HVAC zone dampers",
        "whole house cooling", "whole house heating", "new construction HVAC",
        "home addition HVAC", "basement HVAC", "attic air handler", "crawl space HVAC",
        "basement furnace replacement", "closet air handler installation", "sunroom AC",
        "garage HVAC", "workshop heating cooling", "evaporator coil cleaning",
        "condenser coil cleaning", "AC coil cleaning", "air handler cleaning",
        "HVAC drain pan cleaning", "HVAC filter 16x25", "HVAC filter 20x25", "MERV 13 filter",
        "MERV 16 filter", "biannual HVAC service", "run capacitor replacement",
        "start capacitor replacement", "dual run capacitor", "TXV replacement",
        "electronic expansion valve", "crankcase heater replacement", "defrost control board",
        "control board replacement HVAC", "disconnect box replacement", "refrigerant recovery",
        "nitrogen pressure test HVAC", "condensate pump replacement", "float switch HVAC",
        "secondary drain pan", "drain pan overflow", "AC not turning on", "heat won't come on",
        "AC takes too long to cool", "AC running all night", "humidity too high inside",
        "condensate overflow", "AC only cools sometimes", "HVAC cycles on and off",
        "furnace clicking", "furnace humming", "furnace rumbling", "AC hissing noise",
        "AC gurgling noise", "best AC company near me", "affordable HVAC near me",
        "duct cleaning near me", "AC replacement near me", "furnace replacement near me",
        "heat pump installation near me", "cheap HVAC near me", "HVAC tune up near me",
        "commercial refrigeration repair", "walk-in cooler repair",
        "commercial freezer repair", "industrial HVAC", "school HVAC", "hospital HVAC",
        "medical office HVAC", "retail store HVAC", "restaurant HVAC repair",
        "commercial HVAC maintenance contract", "Google Home thermostat", "HomeKit thermostat",
        "Honeywell thermostat repair", "Honeywell thermostat installation",
        "Alexa HVAC control", "smart AC controller", "0 down HVAC financing",
        "HVAC lease program", "no interest HVAC", "HVAC monthly payment",
        "heat pump federal tax credit", "HVAC utility rebate", "most reliable AC brand",
        "best AC unit brand", "heat pump pros and cons", "gas vs electric furnace",
        "AC vs heat pump cost", "when to replace HVAC system", "signs AC needs replacement",
        "HVAC lifespan", "how long does furnace last", "how long does AC unit last",
        "average HVAC life expectancy", "HVAC brands ranked", "Carrier AC tune-up",
        "Carrier furnace installation", "Carrier furnace tune-up",
        "Carrier heat pump installation", "Carrier heat pump tune-up", "Trane AC tune-up",
        "Trane furnace installation", "Trane furnace tune-up", "Trane heat pump installation",
        "Trane heat pump tune-up", "Lennox AC tune-up", "Lennox furnace installation",
        "Lennox furnace tune-up", "Lennox heat pump installation", "Lennox heat pump tune-up",
        "Rheem AC installation", "Rheem AC tune-up", "Rheem furnace installation",
        "Rheem furnace tune-up", "Rheem heat pump installation", "Rheem heat pump tune-up",
        "Goodman AC installation", "Goodman AC tune-up", "Goodman furnace installation",
        "Goodman furnace tune-up", "Goodman heat pump repair",
        "Goodman heat pump installation", "Goodman heat pump tune-up", "York AC installation",
        "York AC tune-up", "York furnace installation", "York furnace tune-up",
        "York heat pump installation", "York heat pump tune-up",
        "American Standard AC installation", "American Standard AC tune-up",
        "American Standard furnace installation", "American Standard furnace tune-up",
        "American Standard heat pump repair", "American Standard heat pump installation",
        "American Standard heat pump tune-up", "Bryant AC installation", "Bryant AC tune-up",
        "Bryant furnace installation", "Bryant furnace tune-up", "Bryant heat pump repair",
        "Bryant heat pump installation", "Bryant heat pump tune-up", "Ruud AC installation",
        "Ruud AC tune-up", "Ruud furnace installation", "Ruud furnace tune-up",
        "Ruud heat pump repair", "Ruud heat pump installation", "Ruud heat pump tune-up",
        "Payne AC repair", "Payne AC installation", "Payne AC tune-up", "Payne furnace repair",
        "Payne furnace installation", "Payne furnace tune-up", "Payne heat pump repair",
        "Payne heat pump installation", "Payne heat pump tune-up", "Coleman AC repair",
        "Coleman AC installation", "Coleman AC tune-up", "Coleman furnace repair",
        "Coleman furnace installation", "Coleman furnace tune-up", "Coleman heat pump repair",
        "Coleman heat pump installation", "Coleman heat pump tune-up", "Amana AC repair",
        "Amana AC installation", "Amana AC tune-up", "Amana furnace repair",
        "Amana furnace installation", "Amana furnace tune-up", "Amana heat pump repair",
        "Amana heat pump installation", "Amana heat pump tune-up", "Heil AC repair",
        "Heil AC installation", "Heil AC tune-up", "Heil furnace repair",
        "Heil furnace installation", "Heil furnace tune-up", "Heil heat pump repair",
        "Heil heat pump installation", "Heil heat pump tune-up", "Armstrong AC repair",
        "Armstrong AC installation", "Armstrong AC tune-up", "Armstrong furnace repair",
        "Armstrong furnace installation", "Armstrong furnace tune-up",
        "Armstrong heat pump repair", "Armstrong heat pump installation",
        "Armstrong heat pump tune-up", "Frigidaire AC repair", "Frigidaire AC installation",
        "Frigidaire AC tune-up", "Frigidaire furnace repair",
        "Frigidaire furnace installation", "Frigidaire furnace tune-up",
        "Frigidaire heat pump repair", "Frigidaire heat pump installation",
        "Frigidaire heat pump tune-up", "Comfortmaker AC repair",
        "Comfortmaker AC installation", "Comfortmaker AC tune-up",
        "Comfortmaker furnace repair", "Comfortmaker furnace installation",
        "Comfortmaker furnace tune-up", "Comfortmaker heat pump repair",
        "Comfortmaker heat pump installation", "Comfortmaker heat pump tune-up",
        "Tempstar AC repair", "Tempstar AC installation", "Tempstar AC tune-up",
        "Tempstar furnace repair", "Tempstar furnace installation", "Tempstar furnace tune-up",
        "Tempstar heat pump repair", "Tempstar heat pump installation",
        "Tempstar heat pump tune-up", "Luxaire AC repair", "Luxaire AC installation",
        "Luxaire AC tune-up", "Luxaire furnace repair", "Luxaire furnace installation",
        "Luxaire furnace tune-up", "Luxaire heat pump repair",
        "Luxaire heat pump installation", "Luxaire heat pump tune-up",
        "Daikin mini split installation", "Daikin mini split tune-up",
        "Daikin ductless AC repair", "Daikin ductless AC installation",
        "Daikin mini split maintenance", "Mitsubishi mini split installation",
        "Mitsubishi mini split tune-up", "Mitsubishi ductless AC repair",
        "Mitsubishi ductless AC installation", "Mitsubishi mini split maintenance",
        "LG mini split installation", "LG mini split tune-up", "LG ductless AC repair",
        "LG ductless AC installation", "LG mini split maintenance",
        "Fujitsu mini split repair", "Fujitsu mini split installation",
        "Fujitsu mini split tune-up", "Fujitsu ductless AC repair",
        "Fujitsu ductless AC installation", "Fujitsu mini split maintenance",
        "Gree mini split repair", "Gree mini split installation", "Gree mini split tune-up",
        "Gree ductless AC repair", "Gree ductless AC installation",
        "Gree mini split maintenance", "Midea mini split repair",
        "Midea mini split installation", "Midea mini split tune-up",
        "Midea ductless AC repair", "Midea ductless AC installation",
        "Midea mini split maintenance", "Haier mini split repair",
        "Haier mini split installation", "Haier mini split tune-up",
        "Haier ductless AC repair", "Haier ductless AC installation",
        "Haier mini split maintenance", "MrCool mini split repair",
        "MrCool mini split installation", "MrCool mini split tune-up",
        "MrCool ductless AC repair", "MrCool ductless AC installation",
        "MrCool mini split maintenance", "Pioneer mini split repair",
        "Pioneer mini split installation", "Pioneer mini split tune-up",
        "Pioneer ductless AC repair", "Pioneer ductless AC installation",
        "Pioneer mini split maintenance", "Bosch mini split repair",
        "Bosch mini split installation", "Bosch mini split tune-up",
        "Bosch ductless AC repair", "Bosch ductless AC installation",
        "Bosch mini split maintenance", "Honeywell thermostat troubleshooting",
        "Honeywell thermostat not working", "Honeywell thermostat setup",
        "Nest thermostat repair", "Nest thermostat troubleshooting",
        "Nest thermostat not working", "Nest thermostat setup", "Ecobee thermostat repair",
        "Ecobee thermostat installation", "Ecobee thermostat troubleshooting",
        "Ecobee thermostat not working", "Ecobee thermostat setup",
        "mini split repair near me", "heat pump replacement near me",
        "thermostat installation near me", "boiler repair near me",
        "geothermal installation near me", "commercial HVAC near me",
        "air purifier installation near me", "humidifier installation near me",
        "dehumidifier repair near me", "zoning system installation near me",
        "VRF installation near me", "chiller repair near me", "attic fan installation near me",
        "furnace tune-up near me", "heat pump tune-up near me",
        "ductless mini split repair near me", "package unit repair near me",
        "ductwork installation near me", "mini split installation cost", "ductless AC cost",
        "geothermal system cost", "boiler replacement cost", "zoning system cost",
        "air purifier cost", "humidifier installation cost", "dehumidifier cost",
        "duct sealing cost", "thermostat installation cost", "heat pump tune-up cost",
        "furnace tune-up cost", "VRF system cost", "chiller replacement cost",
        "package unit replacement cost", "AC leaking Freon", "furnace pilot light won't light",
        "heat pump defrost light on", "thermostat says heat on but no heat",
        "AC unit outside not running", "furnace flame sensor dirty",
        "AC condensate line frozen", "mini split error code", "heat pump error code",
        "AC compressor humming not starting", "furnace smells like gas",
        "AC unit tripping GFCI", "heat pump ice buildup", "furnace exhaust smell",
        "AC drain line backed up", "mini split leaking water",
        "heat pump making clicking noise", "furnace blower running constantly",
        "AC low on refrigerant", "heat pump not defrosting", "furnace error code",
        "AC unit vibrating", "heat pump fan not spinning",
        "furnace igniter glowing but not lighting", "AC unit frozen solid",
        "spring HVAC tune-up special", "fall furnace tune-up special",
        "HVAC maintenance plan cost", "annual HVAC service contract",
        "bi-annual HVAC inspection", "HVAC service agreement", "summer AC checkup",
        "winter furnace checkup", "pre-summer AC inspection", "pre-winter furnace inspection",
        "seasonal HVAC changeover",
        "whole home dehumidifier installation", "crawl space dehumidifier",
        "solar attic fan installation", "radiant floor heating installation",
        "hydronic baseboard heating repair", "geothermal heat pump installation",
        "geothermal system repair", "ground source heat pump installation",
        "air source heat pump installation", "in-wall AC installation",
        "through-the-wall AC repair", "PTAC unit repair", "PTAC unit installation",
        "water source heat pump", "chilled beam system repair", "VRF heat recovery system",
        "make-up air unit installation", "energy recovery ventilator repair",
        "HVAC extended warranty", "furnace warranty repair", "HVAC parts warranty",
        "manufacturer warranty HVAC repair", "HVAC labor warranty", "HVAC warranty claim",
        "new construction HVAC installation", "builder HVAC package",
        "spec home HVAC installation", "custom home HVAC design", "HVAC load calculation",
        "Manual J calculation", "duct design new home", "HVAC rough-in inspection",
        "affordable AC repair", "affordable furnace repair", "affordable HVAC company",
        "affordable duct cleaning", "affordable heat pump installation",
        "affordable mini split installation", "affordable AC installation",
        "affordable furnace installation", "affordable HVAC contractor",
        "affordable AC maintenance", "best AC repair", "best furnace repair",
        "best duct cleaning", "best heat pump installation", "best mini split installation",
        "best AC installation", "best furnace installation", "best HVAC contractor",
        "best AC maintenance", "top rated AC repair", "top rated furnace repair",
        "top rated HVAC company", "top rated duct cleaning",
        "top rated heat pump installation", "top rated mini split installation",
        "top rated AC installation", "top rated furnace installation",
        "top rated HVAC contractor", "top rated AC maintenance", "licensed AC repair",
        "licensed furnace repair", "licensed HVAC company", "licensed duct cleaning",
        "licensed heat pump installation", "licensed mini split installation",
        "licensed AC installation", "licensed furnace installation",
        "licensed HVAC contractor", "licensed AC maintenance", "certified AC repair",
        "certified furnace repair", "certified HVAC company", "certified duct cleaning",
        "certified heat pump installation", "certified mini split installation",
        "certified AC installation", "certified furnace installation",
        "certified HVAC contractor", "certified AC maintenance", "24 hour HVAC company",
        "24 hour duct cleaning", "24 hour heat pump installation",
        "24 hour mini split installation", "24 hour AC installation",
        "24 hour furnace installation", "24 hour HVAC contractor", "24 hour AC maintenance",
        "same day furnace repair", "same day HVAC company", "same day duct cleaning",
        "same day heat pump installation", "same day mini split installation",
        "same day AC installation", "same day furnace installation",
        "same day HVAC contractor", "same day AC maintenance", "emergency HVAC company",
        "emergency duct cleaning", "emergency heat pump installation",
        "emergency mini split installation", "emergency AC installation",
        "emergency furnace installation", "emergency HVAC contractor",
        "emergency AC maintenance", "local AC repair", "local furnace repair",
        "local HVAC company", "local duct cleaning", "local heat pump installation",
        "local mini split installation", "local AC installation", "local furnace installation",
        "local HVAC contractor", "local AC maintenance", "family owned AC repair",
        "family owned furnace repair", "family owned HVAC company",
        "family owned duct cleaning", "family owned heat pump installation",
        "family owned mini split installation", "family owned AC installation",
        "family owned furnace installation", "family owned HVAC contractor",
        "family owned AC maintenance", "veteran owned AC repair",
        "veteran owned furnace repair", "veteran owned HVAC company",
        "veteran owned duct cleaning", "veteran owned heat pump installation",
        "veteran owned mini split installation", "veteran owned AC installation",
        "veteran owned furnace installation", "veteran owned HVAC contractor",
        "veteran owned AC maintenance", "trusted AC repair", "trusted furnace repair",
        "trusted HVAC company", "trusted duct cleaning", "trusted heat pump installation",
        "trusted mini split installation", "trusted AC installation",
        "trusted furnace installation", "trusted HVAC contractor", "trusted AC maintenance",
        "reliable AC repair", "reliable furnace repair", "reliable HVAC company",
        "reliable duct cleaning", "reliable heat pump installation",
        "reliable mini split installation", "reliable AC installation",
        "reliable furnace installation", "reliable AC maintenance",
        "HVAC same as cash financing", "HVAC 12 month financing", "HVAC 60 month financing",
        "HVAC credit application", "HVAC financing no credit check", "HVAC lease to own",
        "HVAC company reviews", "top HVAC reviews", "HVAC Google reviews", "HVAC Yelp reviews",
        "BBB accredited HVAC company",
    ],
    "plumbing": [
        "plumber", "emergency plumber", "plumbing company", "drain cleaning",
        "water heater repair", "pipe repair", "leak repair", "plumbing service",
        "water heater installation", "sewer line repair", "toilet repair", "faucet repair",
        "plumbing contractor", "clogged drain", "water heater replacement", "plumbing repair",
        "water leak repair", "burst pipe repair", "pipe leak", "drain repair", "sewer repair",
        "sink repair", "shower repair", "bathtub repair", "garbage disposal repair",
        "water line repair", "gas line repair", "kitchen plumbing repair",
        "bathroom plumbing repair", "24 hour plumber", "emergency plumbing",
        "burst pipe emergency", "water leak emergency", "flood plumber", "weekend plumber",
        "after hours plumber", "same day plumber", "emergency pipe repair",
        "flooded basement plumber", "emergency water heater repair", "water shutoff emergency",
        "24 hour plumbing service", "water damage plumber", "pipe burst repair",
        "drain unclogging", "drain clearing", "hydro jetting", "sewer cleaning",
        "main line cleaning", "kitchen drain cleaning", "bathroom drain cleaning",
        "slow drain", "backed up drain", "drain snake service", "rooter service",
        "floor drain cleaning", "drain jetting", "sewer jetting", "kitchen sink clog",
        "bathroom sink clog", "shower drain clog", "bathtub not draining",
        "p-trap replacement", "tankless water heater", "tankless water heater installation",
        "tankless water heater repair", "water heater service", "hot water heater",
        "electric water heater", "gas water heater", "heat pump water heater",
        "water heater not working", "no hot water", "water heater leaking",
        "water heater flush", "hybrid water heater", "water heater expansion tank",
        "water heater anode rod", "on demand water heater", "water heater pilot light",
        "water heater thermocouple", "water heater element replacement",
        "pressure relief valve water heater", "T&P valve replacement", "descale water heater",
        "water heater sediment flush", "tankless water heater cost",
        "tankless vs tank water heater", "when to replace water heater",
        "water heater recirculation pump", "instant hot water", "point of use water heater",
        "sewer line replacement", "sewer line cleaning", "sewer inspection",
        "sewer camera inspection", "trenchless sewer repair", "main sewer line",
        "sewer backup", "sewage backup", "sewer line clog", "sewer smell", "sewer gas",
        "trenchless pipe lining", "pipe bursting repair", "sewer scope inspection",
        "camera drain inspection", "plumbing installation", "bathroom plumbing",
        "kitchen plumbing", "sink installation", "faucet installation", "toilet installation",
        "shower installation", "bathtub installation", "dishwasher installation",
        "washing machine hookup", "garbage disposal installation",
        "outdoor faucet installation", "hose bib replacement",
        "whole house water filter installation", "bathroom remodel plumbing",
        "kitchen remodel plumbing", "rough in plumbing", "new construction plumbing",
        "home addition plumbing", "walk in tub installation", "walk in shower conversion",
        "pipe replacement", "repiping", "whole house repiping", "copper pipe replacement",
        "PEX pipe installation", "galvanized pipe replacement", "pipe inspection",
        "cast iron pipe replacement", "water main repair", "water main replacement",
        "polybutylene pipe replacement", "lead pipe replacement", "repiping cost",
        "whole house repiping cost", "water softener installation",
        "water filtration installation", "water purifier installation",
        "reverse osmosis installation", "hard water treatment", "water softener repair",
        "whole house water filter", "water conditioner", "under sink water filter",
        "water softener salt", "leak detection", "water leak detection", "slab leak repair",
        "slab leak detection", "underground leak detection", "pinhole leak repair",
        "water meter leak", "water line leak detection", "toilet clogged", "toilet running",
        "toilet overflowing", "toilet rocking", "toilet leaking", "wax ring replacement",
        "flapper replacement", "toilet handle replacement", "toilet constantly running",
        "shower valve repair", "shower valve replacement", "bathtub drain clog",
        "shower pan leak", "tub spout repair", "faucet dripping", "dripping faucet",
        "leaky faucet repair", "faucet cartridge replacement", "shower faucet repair",
        "outdoor faucet leaking", "garbage disposal jammed", "garbage disposal not working",
        "garbage disposal humming", "garbage disposal reset", "sump pump installation",
        "sump pump repair", "sump pump replacement", "backflow preventer", "backflow testing",
        "backflow certification", "low water pressure", "high water pressure",
        "water pressure problems", "pressure reducing valve", "ball valve replacement",
        "angle stop replacement", "supply line replacement", "gas line installation",
        "gas leak repair", "gas line extension", "gas dryer hookup", "gas range hookup",
        "frozen pipes", "frozen pipe thawing", "outdoor spigot repair", "hose bib repair",
        "frost free hose bib", "septic tank pumping", "ejector pump installation",
        "grease trap installation", "grease trap service", "well pump repair",
        "well pump replacement", "water pump pressure tank", "pressure tank replacement",
        "main water line repair", "water meter replacement", "water main shutoff",
        "main shut off valve repair", "gas shut off valve", "gas meter plumber",
        "licensed plumber", "local plumber", "residential plumber", "commercial plumber",
        "master plumber", "best plumber", "24 hour plumbing", "emergency plumbing company",
        "honest plumber", "reliable plumber", "trusted plumber", "plumbing cost",
        "plumber cost", "drain cleaning cost", "water heater cost", "pipe repair cost",
        "plumbing repair cost", "plumber hourly rate", "free plumbing estimate",
        "plumbing financing", "affordable plumber", "plumber near me", "plumbing near me",
        "drain cleaning near me", "emergency plumber near me", "water heater repair near me",
        "clogged drain near me", "plumbing company near me", "24 hour plumber near me",
        "licensed plumber near me", "master plumber near me", "commercial plumbing",
        "commercial drain cleaning", "commercial water heater", "commercial pipe repair",
        "commercial plumbing contractor", "restaurant plumbing", "commercial kitchen plumbing",
        "how long does water heater last", "plumbing maintenance",
        "annual plumbing inspection", "plumbing leak test", "water pressure test",
        "plumbing company reviews", "best plumbing company", "Moen faucet repair",
        "Delta faucet repair", "Kohler faucet repair", "Pfister faucet repair",
        "American Standard faucet", "Kohler toilet repair", "Toto toilet installation",
        "American Standard toilet repair", "Mansfield toilet repair",
        "Bradford White water heater", "Rheem water heater repair", "AO Smith water heater",
        "Navien tankless", "Rinnai tankless repair", "Noritz tankless", "State water heater",
        "bidet installation", "bidet seat installation", "pop-up drain replacement",
        "trip lever drain repair", "toilet tank repair", "toilet fill valve repair",
        "jetted tub repair", "whirlpool tub repair", "steam shower installation",
        "rain shower head installation", "body jet installation", "shower system installation",
        "catch basin cleaning", "yard drain cleaning", "French drain installation",
        "area drain repair", "plumbing video inspection", "drain camera inspection",
        "smoke test plumbing", "plumbing pressure test", "water jetting service",
        "power snaking drain", "plumbing permit", "water heater permit", "gas permit plumbing",
        "plumbing inspection report", "plumbing code inspection", "radiant floor plumber",
        "in-floor heating plumber", "pool plumbing repair", "spa plumbing repair",
        "irrigation backflow preventer", "sprinkler backflow repair",
        "water heater tax credit", "tankless water heater rebate", "plumbing home warranty",
        "water heater financing", "plumbing warranty", "water heater tax credit 2026",
        "Moen shower repair", "Delta shower repair", "Kohler shower repair",
        "Grohe faucet repair", "Hansgrohe faucet", "Price Pfister repair",
        "Moen kitchen faucet repair", "Delta kitchen faucet repair",
        "Kohler kitchen faucet repair", "American Standard shower repair",
        "Bradford White water heater repair", "AO Smith water heater repair",
        "Navien tankless service", "Rinnai tankless service", "Noritz tankless repair",
        "State water heater repair", "Rheem water heater service", "GE water heater repair",
        "Bosch water heater", "Ecosmart tankless repair", "toilet bubbling", "toilet gurgling",
        "toilet not flushing all the way", "toilet phantom flush", "toilet tank sweating",
        "toilet whistling", "toilet double flush", "toilet slow flush", "toilet weak flush",
        "toilet fill valve replacement", "toilet flapper cost", "toilet handle broken",
        "toilet seat replacement", "toilet tank cracked", "toilet bowl cracked",
        "dripping faucet repair", "single handle faucet repair", "two handle faucet repair",
        "kitchen faucet sprayer repair", "pull-down faucet repair", "pull-out faucet repair",
        "touchless faucet installation", "pot filler installation", "bar faucet installation",
        "undermount sink installation", "drop-in sink installation",
        "farmhouse sink installation", "utility sink installation",
        "laundry sink installation", "bathroom vanity installation", "bathtub refinishing",
        "bathtub reglazing", "bathtub liner installation", "freestanding tub installation",
        "soaking tub installation", "shower door installation",
        "frameless shower door installation", "glass shower door repair",
        "shower pan replacement", "shower tray installation", "tree root in sewer line",
        "root removal sewer", "roots blocking drain", "sewer roots treatment",
        "main drain clog", "all drains backing up", "sewage in basement",
        "sewage overflow cleanup", "iron filter installation", "sulfur water treatment",
        "hard water spots", "water softener bypass valve", "water softener not working",
        "water softener regeneration", "well water testing", "well chlorination",
        "well shock treatment", "submersive pump repair", "jet pump repair",
        "well pressure switch", "well tank replacement", "septic system repair",
        "septic field repair", "leach field repair", "septic inspection",
        "septic pumping cost", "septic tank replacement", "gas fireplace line installation",
        "gas fire pit hookup", "gas pool heater hookup", "gas BBQ line installation",
        "natural gas line extension", "outdoor shower installation",
        "anti-siphon valve repair", "yard hydrant installation", "irrigation system plumbing",
        "sprinkler system repair", "drip irrigation installation",
        "water softener installation near me", "sewer repair near me", "pipe repair near me",
        "leak detection near me", "sump pump near me", "garbage disposal near me",
        "water heater installation near me", "tankless water heater near me",
        "how much does drain cleaning cost", "how much is a plumber",
        "how much to replace water heater", "how much does repiping cost",
        "do I need to repipe my house", "how to unclog drain", "signs of slab leak",
        "what causes low water pressure", "how long do pipes last", "when to repipe house",
        "Insinkerator garbage disposal repair", "Insinkerator garbage disposal installation",
        "Insinkerator garbage disposal replacement", "Waste King garbage disposal repair",
        "Waste King garbage disposal installation", "Waste King garbage disposal replacement",
        "Moen garbage disposal repair", "Moen garbage disposal installation",
        "Moen garbage disposal replacement", "GE garbage disposal repair",
        "GE garbage disposal installation", "GE garbage disposal replacement",
        "Kohler toilet installation", "Kohler toilet replacement",
        "Kohler toilet not flushing repair", "Toto toilet repair", "Toto toilet replacement",
        "Toto toilet not flushing repair", "American Standard toilet installation",
        "American Standard toilet replacement", "American Standard toilet not flushing repair",
        "Mansfield toilet installation", "Mansfield toilet replacement",
        "Mansfield toilet not flushing repair", "Gerber toilet installation",
        "Gerber toilet repair", "Gerber toilet replacement",
        "Gerber toilet not flushing repair", "Eljer toilet installation",
        "Eljer toilet repair", "Eljer toilet replacement", "Eljer toilet not flushing repair",
        "Niagara toilet installation", "Niagara toilet repair", "Niagara toilet replacement",
        "Niagara toilet not flushing repair", "Woodbridge toilet installation",
        "Woodbridge toilet repair", "Woodbridge toilet replacement",
        "Woodbridge toilet not flushing repair", "Swiss Madison toilet installation",
        "Swiss Madison toilet repair", "Swiss Madison toilet replacement",
        "Swiss Madison toilet not flushing repair", "Moen faucet installation",
        "Moen faucet replacement", "Moen faucet cartridge replacement",
        "Delta faucet installation", "Delta faucet replacement",
        "Delta faucet cartridge replacement", "Kohler faucet installation",
        "Kohler faucet replacement", "Kohler faucet cartridge replacement",
        "Pfister faucet installation", "Pfister faucet replacement",
        "Pfister faucet cartridge replacement", "Grohe faucet installation",
        "Grohe faucet replacement", "Grohe faucet cartridge replacement",
        "Hansgrohe faucet repair", "Hansgrohe faucet installation",
        "Hansgrohe faucet replacement", "Hansgrohe faucet cartridge replacement",
        "American Standard faucet repair", "American Standard faucet installation",
        "American Standard faucet replacement",
        "American Standard faucet cartridge replacement", "Symmons faucet repair",
        "Symmons faucet installation", "Symmons faucet replacement",
        "Symmons faucet cartridge replacement", "Waterstone faucet repair",
        "Waterstone faucet installation", "Waterstone faucet replacement",
        "Waterstone faucet cartridge replacement", "Kraus faucet repair",
        "Kraus faucet installation", "Kraus faucet replacement",
        "Kraus faucet cartridge replacement", "Blanco faucet repair",
        "Blanco faucet installation", "Blanco faucet replacement",
        "Blanco faucet cartridge replacement", "Franke faucet repair",
        "Franke faucet installation", "Franke faucet replacement",
        "Franke faucet cartridge replacement", "Bradford White water heater installation",
        "Bradford White water heater replacement", "Bradford White water heater maintenance",
        "Bradford White tankless water heater repair",
        "Bradford White tankless water heater installation", "Rheem water heater installation",
        "Rheem water heater replacement", "Rheem water heater maintenance",
        "Rheem tankless water heater repair", "Rheem tankless water heater installation",
        "AO Smith water heater installation", "AO Smith water heater replacement",
        "AO Smith water heater maintenance", "AO Smith tankless water heater repair",
        "AO Smith tankless water heater installation", "Navien water heater repair",
        "Navien water heater installation", "Navien water heater replacement",
        "Navien water heater maintenance", "Navien tankless water heater repair",
        "Navien tankless water heater installation", "Rinnai water heater repair",
        "Rinnai water heater installation", "Rinnai water heater replacement",
        "Rinnai water heater maintenance", "Rinnai tankless water heater repair",
        "Rinnai tankless water heater installation", "Noritz water heater repair",
        "Noritz water heater installation", "Noritz water heater replacement",
        "Noritz water heater maintenance", "Noritz tankless water heater repair",
        "Noritz tankless water heater installation", "State water heater installation",
        "State water heater replacement", "State water heater maintenance",
        "State tankless water heater repair", "State tankless water heater installation",
        "GE water heater installation", "GE water heater replacement",
        "GE water heater maintenance", "GE tankless water heater repair",
        "GE tankless water heater installation", "Bosch water heater repair",
        "Bosch water heater installation", "Bosch water heater replacement",
        "Bosch water heater maintenance", "Bosch tankless water heater repair",
        "Bosch tankless water heater installation", "Ecosmart water heater repair",
        "Ecosmart water heater installation", "Ecosmart water heater replacement",
        "Ecosmart water heater maintenance", "Ecosmart tankless water heater repair",
        "Ecosmart tankless water heater installation", "American Standard water heater repair",
        "American Standard water heater installation",
        "American Standard water heater replacement",
        "American Standard water heater maintenance",
        "American Standard tankless water heater repair",
        "American Standard tankless water heater installation", "Elkay sink installation",
        "Elkay sink repair", "Kohler sink installation", "Kohler sink repair",
        "Blanco sink installation", "Blanco sink repair", "Franke sink installation",
        "Franke sink repair", "Kraus sink installation", "Kraus sink repair",
        "Swanstone sink installation", "Swanstone sink repair",
        "Culligan water softener installation", "Culligan water softener repair",
        "Culligan water softener maintenance", "Kinetico water softener installation",
        "Kinetico water softener repair", "Kinetico water softener maintenance",
        "Aquasana water softener installation", "Aquasana water softener repair",
        "Aquasana water softener maintenance", "iSpring water softener installation",
        "iSpring water softener repair", "iSpring water softener maintenance",
        "Whirlpool water softener installation", "Whirlpool water softener repair",
        "Whirlpool water softener maintenance", "GE water softener installation",
        "GE water softener repair", "GE water softener maintenance",
        "Fleck water softener installation", "Fleck water softener repair",
        "Fleck water softener maintenance", "Pentair water softener installation",
        "Pentair water softener repair", "Pentair water softener maintenance",
        "copper pipe repair", "copper pipe installation", "PEX pipe repair",
        "PEX pipe replacement", "PVC pipe repair", "PVC pipe replacement",
        "PVC pipe installation", "CPVC pipe repair", "CPVC pipe replacement",
        "CPVC pipe installation", "galvanized pipe repair", "galvanized pipe installation",
        "cast iron pipe repair", "cast iron pipe installation", "polybutylene pipe repair",
        "polybutylene pipe installation", "lead pipe repair", "lead pipe installation",
        "kitchen sink drain repair", "kitchen sink drain replacement",
        "kitchen sink drain installation", "bathroom sink drain repair",
        "bathroom sink drain replacement", "bathroom sink drain installation",
        "shower drain repair", "shower drain replacement", "shower drain installation",
        "bathtub drain repair", "bathtub drain replacement", "bathtub drain installation",
        "floor drain repair", "floor drain replacement", "floor drain installation",
        "laundry drain repair", "laundry drain replacement", "laundry drain installation",
        "garage drain repair", "garage drain replacement", "garage drain installation",
        "yard drain repair", "yard drain replacement", "yard drain installation",
        "area drain replacement", "area drain installation", "french drain repair",
        "french drain replacement", "repiping near me", "slab leak repair near me",
        "water softener repair near me", "backflow testing near me", "hydro jetting near me",
        "septic pumping near me", "well pump repair near me", "gas line repair near me",
        "toilet installation near me", "faucet repair near me", "bidet installation near me",
        "sump pump installation near me", "french drain installation near me",
        "toilet repair near me", "faucet installation near me",
        "garbage disposal repair near me", "water heater replacement near me",
        "pipe replacement near me", "gas leak repair near me", "shower installation near me",
        "bathtub installation near me", "kitchen plumbing near me",
        "bathroom plumbing near me", "backflow preventer near me", "irrigation repair near me",
        "sprinkler repair near me", "well pump installation near me",
        "septic tank repair near me", "grease trap cleaning near me", "repiping cost per foot",
        "slab leak repair cost", "hydro jetting cost", "backflow testing cost",
        "well pump replacement cost", "gas line installation cost", "bidet installation cost",
        "french drain cost", "sump pump installation cost", "water softener cost",
        "water filtration system cost", "toilet installation cost", "faucet installation cost",
        "garbage disposal installation cost", "shower installation cost",
        "bathtub installation cost", "sink installation cost", "backflow preventer cost",
        "irrigation repair cost", "well pump installation cost", "septic tank repair cost",
        "grease trap cleaning cost", "gurgling toilet when sink drains",
        "sewer smell in bathroom", "water heater making popping noise",
        "water heater leaking from bottom", "water heater leaking from top",
        "low hot water pressure", "hot water runs out fast", "toilet won't stop running",
        "toilet tank not filling", "faucet handle stuck", "faucet won't turn off",
        "garbage disposal leaking", "garbage disposal smells bad", "dishwasher not draining",
        "washing machine drain backing up", "water hammer noise pipes",
        "banging pipes when water shut off", "air in pipes", "shower drain smells like sewage",
        "bathroom smells like sewage", "water bill suddenly high",
        "water meter spinning no water running", "toilet rocks when sitting",
        "toilet base leaking at floor", "water spots on ceiling below bathroom",
        "brown water from faucet", "rusty water from tap", "air bubbles in faucet water",
        "low flow from all faucets", "only cold water no hot water",
        "water heater tripping breaker", "water heater pilot light won't stay lit",
        "smell of gas near water heater", "winterize outdoor faucets",
        "spring plumbing checkup", "fall plumbing maintenance",
        "annual plumbing inspection cost", "pre-listing plumbing inspection",
        "home inspection plumbing repair", "holiday plumbing checklist",
        "before hosting guests plumbing check", "new home plumbing inspection",
        "move-in plumbing inspection", "water heater expansion tank installation",
        "point of use water heater installation", "recirculating hot water system",
        "hot water recirculation pump installation", "commercial grease trap pumping",
        "medical gas plumbing", "laboratory plumbing", "clean room plumbing",
        "fire sprinkler plumbing", "backwater valve installation", "check valve installation",
        "mixing valve installation", "thermostatic mixing valve installation",
        "pressure balancing valve repair", "anti-scald valve installation",
        "water hammer arrestor installation", "expansion tank replacement",
        "pressure reducing valve installation", "emergency shut off valve installation",
        "whole house shut off valve installation", "gas appliance hookup",
        "dishwasher installation plumbing", "ice maker line installation",
        "refrigerator water line installation", "outdoor kitchen sink installation",
        "wet bar plumbing installation", "laundry room plumbing rough-in",
        "affordable plumbing company", "affordable drain cleaning",
        "affordable water heater repair", "affordable leak detection",
        "affordable sewer repair", "affordable pipe repair", "affordable emergency plumbing",
        "affordable toilet repair", "affordable faucet repair",
        "affordable water softener installation", "affordable backflow testing",
        "affordable sump pump installation", "affordable garbage disposal repair",
        "best drain cleaning", "best water heater repair", "best leak detection",
        "best sewer repair", "best pipe repair", "best emergency plumbing",
        "best toilet repair", "best faucet repair", "best water softener installation",
        "best backflow testing", "best sump pump installation", "best garbage disposal repair",
        "top rated plumber", "top rated plumbing company", "top rated drain cleaning",
        "top rated water heater repair", "top rated leak detection", "top rated sewer repair",
        "top rated pipe repair", "top rated emergency plumbing", "top rated toilet repair",
        "top rated faucet repair", "top rated water softener installation",
        "top rated backflow testing", "top rated sump pump installation",
        "top rated garbage disposal repair", "licensed plumbing company",
        "licensed drain cleaning", "licensed water heater repair", "licensed leak detection",
        "licensed sewer repair", "licensed pipe repair", "licensed emergency plumbing",
        "licensed toilet repair", "licensed faucet repair",
        "licensed water softener installation", "licensed backflow testing",
        "licensed sump pump installation", "licensed garbage disposal repair",
        "certified plumber", "certified plumbing company", "certified drain cleaning",
        "certified water heater repair", "certified leak detection", "certified sewer repair",
        "certified pipe repair", "certified emergency plumbing", "certified toilet repair",
        "certified faucet repair", "certified water softener installation",
        "certified backflow testing", "certified sump pump installation",
        "certified garbage disposal repair", "24 hour plumbing company",
        "24 hour drain cleaning", "24 hour water heater repair", "24 hour leak detection",
        "24 hour sewer repair", "24 hour pipe repair", "24 hour emergency plumbing",
        "24 hour toilet repair", "24 hour faucet repair",
        "24 hour water softener installation", "24 hour backflow testing",
        "24 hour sump pump installation", "24 hour garbage disposal repair",
        "same day plumbing company", "same day drain cleaning", "same day water heater repair",
        "same day leak detection", "same day sewer repair", "same day pipe repair",
        "same day emergency plumbing", "same day toilet repair", "same day faucet repair",
        "same day water softener installation", "same day backflow testing",
        "same day sump pump installation", "same day garbage disposal repair",
        "emergency drain cleaning", "emergency leak detection", "emergency sewer repair",
        "emergency toilet repair", "emergency faucet repair",
        "emergency water softener installation", "emergency backflow testing",
        "emergency sump pump installation", "emergency garbage disposal repair",
        "local plumbing company", "local drain cleaning", "local water heater repair",
        "local leak detection", "local sewer repair", "local pipe repair",
        "local emergency plumbing", "local toilet repair", "local faucet repair",
        "local water softener installation", "local backflow testing",
        "local sump pump installation", "local garbage disposal repair",
        "family owned plumber", "family owned plumbing company", "family owned drain cleaning",
        "family owned water heater repair", "family owned leak detection",
        "family owned sewer repair", "family owned pipe repair",
        "family owned emergency plumbing", "family owned toilet repair",
        "family owned faucet repair", "family owned water softener installation",
        "family owned backflow testing", "family owned sump pump installation",
        "family owned garbage disposal repair", "veteran owned plumber",
        "veteran owned plumbing company", "veteran owned drain cleaning",
        "veteran owned water heater repair", "veteran owned leak detection",
        "veteran owned sewer repair", "veteran owned pipe repair",
        "veteran owned emergency plumbing", "veteran owned toilet repair",
        "veteran owned faucet repair", "veteran owned water softener installation",
        "veteran owned backflow testing", "veteran owned sump pump installation",
        "veteran owned garbage disposal repair", "trusted plumbing company",
        "trusted drain cleaning", "trusted water heater repair", "trusted leak detection",
        "trusted sewer repair", "trusted pipe repair", "trusted emergency plumbing",
        "trusted toilet repair", "trusted faucet repair",
        "trusted water softener installation", "trusted backflow testing",
        "trusted sump pump installation", "trusted garbage disposal repair",
        "reliable plumbing company", "reliable drain cleaning", "reliable water heater repair",
        "reliable leak detection", "reliable sewer repair", "reliable pipe repair",
        "reliable emergency plumbing", "reliable toilet repair", "reliable faucet repair",
        "reliable water softener installation", "reliable backflow testing",
        "reliable sump pump installation", "reliable garbage disposal repair",
        "restaurant grease trap service", "hotel plumbing repair",
        "apartment complex plumbing", "office building plumbing", "retail plumbing repair",
        "medical office plumbing", "school plumbing repair", "gym locker room plumbing",
        "plumbing financing no credit check", "plumbing same as cash financing",
        "water heater financing options", "repiping financing", "top rated plumber reviews",
        "BBB accredited plumber", "A+ rated plumbing company", "licensed and insured plumber",
        "plumbing Google reviews", "compare plumbing quotes", "get multiple plumbing quotes",
        "free second opinion plumber", "plumber service call fee", "plumbing dispatch fee",
        "weekend plumbing surcharge", "holiday plumbing rate", "plumbing inspection checklist",
        "plumbing code violation repair", "plumbing permit cost",
        "water pressure regulator installation",
    ],
    "roofing": [
        "roofing company", "roof repair", "roof replacement", "roofer",
        "storm damage roof repair", "roofing contractor", "roof inspection",
        "shingle replacement", "flat roof repair", "roofing service", "emergency roof repair",
        "gutter installation", "roof leak repair", "new roof installation", "roofing estimate",
        "hail damage roof repair", "wind damage roof repair", "shingle repair",
        "metal roof repair", "tile roof repair", "roof patching", "roof flashing repair",
        "gutter repair", "drip edge repair", "roof valley repair", "chimney flashing repair",
        "new roof", "roof installation", "full roof replacement", "metal roof installation",
        "flat roof installation", "roof reroof", "roof overlay",
        "standing seam metal roof installation", "complete roof replacement",
        "shingle installation", "tile roof installation", "TPO roof installation",
        "hail damage roof", "wind damage roof", "insurance roof claim", "hail damage shingles",
        "storm damaged shingles", "emergency roof tarping", "storm roof inspection",
        "insurance roofing contractor", "roof after hail storm", "storm damage assessment",
        "roofing insurance claim help", "insurance approved roofer",
        "insurance roof replacement", "storm chaser roofer", "roof supplement", "local roofer",
        "licensed roofer", "residential roofer", "commercial roofer", "roofing professional",
        "best roofing company", "roofing specialist", "certified roofer",
        "roofing professionals", "GAF certified contractor",
        "Owens Corning preferred contractor", "manufacturer certified roofer",
        "veteran owned roofing", "family owned roofing company", "top rated roofing company",
        "honest roofing contractor", "reliable roofer", "free roof inspection",
        "roof assessment", "roof evaluation", "free roofing estimate", "roof leak inspection",
        "roof certification", "post-storm roof inspection", "roof age assessment",
        "roof replacement inspection", "roof inspection report", "satellite roof measurement",
        "aerial roof measurement", "gutter replacement", "seamless gutters",
        "gutter guard installation", "gutter cleaning", "downspout repair",
        "leaf guard installation", "gutter protection", "K-style gutters",
        "half-round gutters", "gutter helmet", "gutter covers", "LeafFilter installation",
        "gutter system installation", "copper gutters", "downspout extension",
        "gutter downspout installation", "asphalt shingles", "architectural shingles",
        "3-tab shingles", "metal roofing", "standing seam metal roof", "tile roofing",
        "clay tile roof", "concrete tile roof", "flat roof membrane", "TPO roofing",
        "EPDM roofing", "modified bitumen roofing", "rubber roof", "composite shingles",
        "impact resistant shingles", "GAF shingles", "Owens Corning shingles",
        "CertainTeed shingles", "Class 4 shingles", "50 year shingles", "30 year shingles",
        "lifetime shingles", "dimensional shingles", "GAF Timberline HDZ",
        "Owens Corning Duration shingles", "CertainTeed Landmark shingles", "Atlas shingles",
        "metal shake shingles", "corrugated metal roofing", "aluminum roofing",
        "copper roofing", "spray foam roofing", "PVC roofing", "torch down roofing",
        "built-up roofing BUR", "attic insulation", "attic ventilation",
        "ridge vent installation", "attic fan installation", "roof ventilation",
        "attic inspection", "soffit vents", "ice dam removal", "ice dam prevention",
        "roof deck replacement", "attic air sealing", "attic mold remediation",
        "wet insulation attic", "hot attic repair", "roof ventilation problems", "solar roof",
        "skylight installation", "skylight repair", "chimney flashing", "chimney repair",
        "chimney cap installation", "fascia repair", "soffit repair", "roof coating",
        "flat roof coating", "roof restoration", "roof sealing", "cool roof coating",
        "silicone roof coating", "reflective roof coating", "spray foam roof coating",
        "roof waterproofing", "skylight leak repair", "dormer repair",
        "shed dormer installation", "roof replacement cost", "new roof cost", "roofing cost",
        "shingle cost", "metal roof cost", "roof repair cost", "average roof replacement cost",
        "cost to replace roof", "roof financing", "roofing materials cost",
        "roofing labor cost", "roofing price per square", "metal roof vs shingles cost",
        "roof payment plan", "0 down roofing", "roofing financing options",
        "GreenSky roofing financing", "roofing company near me", "roofer near me",
        "roof repair near me", "roof replacement near me", "roofing contractor near me",
        "roof inspection near me", "roofing estimate near me", "local roofing company",
        "24 hour roofer", "same day roofing", "emergency roofer near me",
        "roof leak repair near me", "commercial roofing", "commercial roof repair",
        "commercial roof replacement", "TPO roofing installation", "built-up roofing",
        "EPDM installation", "industrial roofing", "flat roof commercial", "low slope roofing",
        "commercial roof inspection", "commercial roof maintenance", "annual roof inspection",
        "preventive roof maintenance", "roof leaking", "water coming through ceiling",
        "missing shingles", "curling shingles", "cracked shingles", "granule loss shingles",
        "moss on roof", "algae on roof", "sagging roof", "roof damage", "when to replace roof",
        "roof lifespan", "how long does a roof last", "old roof replacement",
        "black streaks on roof", "dark stains roof", "peeling paint ceiling leak",
        "water stain ceiling", "soft spots roof", "rotted decking repair", "mold on roof",
        "roof after heavy rain", "pipe boot replacement", "vent flashing repair",
        "valley flashing", "step flashing repair", "underlayment replacement",
        "ice and water shield", "roof decking replacement", "ridge cap replacement",
        "hip cap shingles", "starter strip shingles", "roofing nails", "rafter repair",
        "truss repair", "structural roof repair", "ridge board replacement",
        "roof truss repair", "roof repair vs replacement", "when to replace shingles",
        "metal roof vs shingles", "best roofing material", "most durable roofing",
        "energy efficient roofing", "energy star shingles", "algae resistant shingles",
        "StainGuard shingles", "roof cleaning service", "roof soft wash",
        "moss treatment roof", "roof warranty", "labor warranty roofing",
        "roofing company BBB", "A rated roofer", "how to choose a roofer",
        "roofing company reviews", "wood shake roof repair", "cedar shake replacement",
        "slate roof repair", "slate roof replacement", "natural slate roofing",
        "synthetic slate roofing", "rubber slate shingles", "composite slate roofing",
        "Tamko shingles", "Atlas StormMaster", "IKO shingles", "PABCO shingles",
        "green roof installation", "living roof", "vegetative roof", "EPDM patch repair",
        "TPO seam repair", "liquid rubber roofing", "flat roof blister repair",
        "flat roof membrane patch", "bitumen roofing repair", "roofing felt replacement",
        "multi-family roofing", "apartment complex roofing", "condo roof repair",
        "townhouse roof repair", "church roof repair", "school roof repair",
        "warehouse roof repair", "retail building roofing", "commercial roof coating",
        "annual commercial roof inspection", "snow load roof repair",
        "roof snow removal service", "ice dam specialist", "roof rake service",
        "cold weather roofing", "winter roof repair", "ceiling bubbling paint roof leak",
        "roof deck wet", "attic condensation repair", "nail pops roof repair",
        "spongy roof deck", "lichen on roof removal", "green stains roof",
        "emergency tarp service", "temporary roof repair", "roof felt exposed",
        "roofing permit", "permit for new roof", "HOA roof approval",
        "HOA approved roofing materials", "cool roof rebate", "roofing tax credit",
        "energy efficient roofing rebate", "roof financing options",
        "roofing insurance deductible", "GAF financing", "free roof estimate near me",
        "roof cleaning near me", "gutter cleaning near me", "seamless gutter near me",
        "gutter guard near me", "ice dam removal near me", "GAF roof installation",
        "GAF shingle repair", "GAF roof replacement", "GAF Master Elite contractor",
        "GAF warranty", "Owens Corning roof installation", "Owens Corning shingle repair",
        "Owens Corning Platinum preferred", "Owens Corning warranty",
        "CertainTeed roof installation", "CertainTeed shingle repair",
        "CertainTeed SELECT ShingleMaster", "Atlas roof installation",
        "Atlas StormMaster Slate", "Tamko Heritage shingles", "Tamko roof repair",
        "Malarkey shingles", "Elk shingles", "DECRA roofing", "standing seam repair",
        "metal panel roofing repair", "corrugated metal roof repair", "R-panel roofing",
        "exposed fastener metal roof", "metal roof panel replacement",
        "metal roof screw replacement", "metal roof rust repair", "Galvalume roofing",
        "Corten steel roofing", "metal roof paint", "metal roof restoration",
        "HVAC curb roofing", "roof penetration sealing", "coping cap repair",
        "parapet wall waterproofing", "roof drain installation", "interior roof drain",
        "roof hatch installation", "walk pad roofing", "multi-family roofing contractor",
        "apartment complex roof replacement", "HOA roofing contractor",
        "property management roofing", "school roof replacement", "retail building roof",
        "hotel roofing", "office building roofing", "roof bubbling", "flat roof ponding water",
        "flat roof standing water", "roof sagging middle", "ceiling water ring",
        "ceiling water stain", "water coming in around chimney",
        "water coming in around skylight", "nail pops shingles", "fastener blowout roofing",
        "roof feels spongy", "soft spot on roof", "green stains on roof", "lichen on roof",
        "roof granules in gutter", "shingle granule loss", "RV roof repair", "carport roofing",
        "pergola roofing", "patio cover roofing", "sunroom roof repair", "pole barn roofing",
        "metal building roofing", "shed roofing", "detached garage roofing",
        "gutter downspout replacement", "downspout underground drainage",
        "splash block installation", "gutter elbow replacement", "gutter spike replacement",
        "gutter hanger installation", "gutter slope correction", "gutter overflow",
        "gutter pulling away from house", "fascia board replacement", "soffit replacement",
        "eave repair", "rake board replacement", "exterior trim repair",
        "drip edge replacement", "window flashing repair", "door flashing repair",
        "wall flashing repair", "siding and roofing", "metal roofer near me",
        "TPO roofer near me", "flat roof specialist near me", "commercial roofer near me",
        "hail damage roofer near me", "storm damage roofer near me",
        "gutter installer near me", "LeafFilter near me", "roofing permit cost",
        "HOA approved shingles", "how to file roof insurance claim",
        "roof insurance claim process", "does insurance cover roof replacement",
        "when does insurance cover roof", "impact resistant shingles discount",
        "hail resistant roof discount", "how many squares is my roof",
        "roofing square calculator", "roof measurement tool",
        "how to measure roof for shingles", "DIY roof repair", "temporary roof fix",
        "roof patch kit", "roof sealant", "how long does roof repair take",
        "how long to replace a roof", "roofing season", "best time to replace roof",
        "GAF roof inspection", "GAF roof warranty claim", "GAF roof financing",
        "GAF shingle color match", "GAF roof repair", "GAF gutter installation",
        "Owens Corning roof inspection", "Owens Corning roof warranty claim",
        "Owens Corning roof financing", "Owens Corning shingle color match",
        "Owens Corning roof repair", "Owens Corning roof replacement",
        "Owens Corning gutter installation", "CertainTeed roof inspection",
        "CertainTeed roof warranty claim", "CertainTeed roof financing",
        "CertainTeed shingle color match", "CertainTeed roof repair",
        "CertainTeed roof replacement", "CertainTeed gutter installation",
        "Atlas roof inspection", "Atlas roof warranty claim", "Atlas roof financing",
        "Atlas shingle color match", "Atlas roof repair", "Atlas roof replacement",
        "Atlas shingle repair", "Atlas gutter installation", "Tamko roof inspection",
        "Tamko roof warranty claim", "Tamko roof financing", "Tamko shingle color match",
        "Tamko roof replacement", "Tamko roof installation", "Tamko shingle repair",
        "Tamko gutter installation", "Malarkey roof inspection",
        "Malarkey roof warranty claim", "Malarkey roof financing",
        "Malarkey shingle color match", "Malarkey roof repair", "Malarkey roof replacement",
        "Malarkey roof installation", "Malarkey shingle repair",
        "Malarkey gutter installation", "IKO roof inspection", "IKO roof warranty claim",
        "IKO roof financing", "IKO shingle color match", "IKO roof repair",
        "IKO roof replacement", "IKO roof installation", "IKO shingle repair",
        "IKO gutter installation", "PABCO roof inspection", "PABCO roof warranty claim",
        "PABCO roof financing", "PABCO shingle color match", "PABCO roof repair",
        "PABCO roof replacement", "PABCO roof installation", "PABCO shingle repair",
        "PABCO gutter installation", "Elk roof inspection", "Elk roof warranty claim",
        "Elk roof financing", "Elk shingle color match", "Elk roof repair",
        "Elk roof replacement", "Elk roof installation", "Elk shingle repair",
        "Elk gutter installation", "Metal Sales metal roofing installation",
        "Metal Sales metal roof repair", "Metal Sales standing seam installation",
        "Metal Sales metal roof warranty", "McElroy Metal standing seam installation",
        "Englert metal roofing installation", "Englert metal roof repair",
        "Englert standing seam installation", "Englert metal roof warranty",
        "ATAS metal roofing installation", "ATAS metal roof repair",
        "ATAS standing seam installation", "ATAS metal roof warranty",
        "Firestone metal roofing installation", "Firestone metal roof repair",
        "Firestone standing seam installation", "Firestone metal roof warranty",
        "Carlisle metal roofing installation", "Carlisle metal roof repair",
        "Carlisle standing seam installation", "Carlisle metal roof warranty",
        "Duro-Last metal roofing installation", "Duro-Last metal roof repair",
        "Duro-Last standing seam installation", "Duro-Last metal roof warranty",
        "Firestone TPO installation", "Firestone EPDM installation",
        "Firestone roof coating system", "Firestone single ply roofing",
        "Carlisle TPO installation", "Carlisle EPDM installation",
        "Carlisle roof coating system", "Carlisle single ply roofing",
        "Johns Manville TPO installation", "Johns Manville EPDM installation",
        "Johns Manville roof coating system", "Johns Manville single ply roofing",
        "Duro-Last TPO installation", "Duro-Last EPDM installation",
        "Duro-Last roof coating system", "Duro-Last single ply roofing",
        "GAF TPO installation", "GAF EPDM installation", "GAF roof coating system",
        "GAF single ply roofing", "asphalt shingle roof repair",
        "asphalt shingle roof replacement", "asphalt shingle roof installation",
        "asphalt shingle roof inspection", "asphalt shingle roof maintenance",
        "architectural shingle roof repair", "architectural shingle roof replacement",
        "architectural shingle roof installation", "architectural shingle roof inspection",
        "architectural shingle roof maintenance", "metal roof replacement",
        "metal roof inspection", "metal roof maintenance", "tile roof replacement",
        "tile roof inspection", "tile roof maintenance", "slate roof installation",
        "slate roof inspection", "slate roof maintenance", "cedar shake roof repair",
        "cedar shake roof replacement", "cedar shake roof installation",
        "cedar shake roof inspection", "cedar shake roof maintenance", "TPO roof repair",
        "TPO roof replacement", "TPO roof inspection", "TPO roof maintenance",
        "EPDM roof repair", "EPDM roof replacement", "EPDM roof installation",
        "EPDM roof inspection", "EPDM roof maintenance", "PVC roof repair",
        "PVC roof replacement", "PVC roof installation", "PVC roof inspection",
        "PVC roof maintenance", "modified bitumen roof repair",
        "modified bitumen roof replacement", "modified bitumen roof installation",
        "modified bitumen roof inspection", "modified bitumen roof maintenance",
        "roof coating near me", "skylight repair near me", "chimney flashing repair near me",
        "attic insulation near me", "solar roof installation near me",
        "slate roof repair near me", "cedar shake repair near me", "roof financing near me",
        "shingle repair near me", "roof replacement financing near me",
        "metal roof installation near me", "tile roof repair near me",
        "commercial roofing near me", "free roof inspection near me",
        "emergency roof tarping near me", "gutter guard installation near me",
        "roof coating cost", "skylight installation cost", "chimney flashing repair cost",
        "attic insulation cost", "solar roof cost", "slate roof cost", "cedar shake roof cost",
        "synthetic slate cost", "standing seam metal roof cost", "roof underlayment cost",
        "shingle replacement cost", "tile roof replacement cost", "flat roof replacement cost",
        "TPO roof cost", "EPDM roof cost", "built-up roof cost", "modified bitumen cost",
        "roof tear off cost", "roof decking replacement cost", "roof felt cost",
        "roof leaking after rain", "ceiling stain getting bigger",
        "shingles blown off in wind", "roof shingles curling up",
        "granules in gutter after storm", "roof sagging near chimney",
        "daylight visible in attic", "attic smells musty after rain", "ice buildup on eaves",
        "water pooling on flat roof", "roof tarp blew off", "shingles missing after storm",
        "new roof already leaking", "roof leak only when raining hard",
        "attic insulation wet from leak", "roof leak near vent pipe",
        "roof leak near satellite dish mount", "roof leak around solar panels",
        "pre-winter roof inspection", "spring roof checkup", "hurricane season roof prep",
        "roof prep before selling house", "pre-listing roof inspection",
        "copper flashing installation", "lead flashing repair", "chimney cricket installation",
        "cricket flashing repair", "roof to wall flashing", "kickout flashing installation",
        "roof jack installation", "turbine vent installation", "static vent installation",
        "box vent installation", "power vent installation", "solar attic fan installation",
        "radiant barrier installation", "roof deck ventilation baffle", "roofing loan options",
        "roof replacement financing no credit check", "0 percent roofing financing",
        "roofing home equity loan", "top rated roofer reviews", "BBB accredited roofer",
        "A+ rated roofing company", "GAF Master Elite reviews", "roofing Google reviews",
        "compare roofing quotes", "get multiple roofing quotes", "free second opinion roofer",
        "roofing Angi reviews", "roofing HomeAdvisor reviews",
        "roofing Nextdoor recommendations", "roof replacement testimonials",
        "roofing company case studies", "roofing manufacturer warranty transfer",
        "roof workmanship warranty", "roofing permit inspection",
        "roof replacement permit requirements", "affordable roofing company",
        "affordable roof repair", "affordable roof replacement",
        "affordable roofing contractor", "affordable gutter installation",
        "affordable roof inspection", "affordable emergency roof repair",
        "affordable metal roof installation", "affordable flat roof repair",
        "affordable roof coating", "affordable commercial roof repair",
        "affordable chimney flashing repair", "best roof repair", "best roof replacement",
        "best roofing contractor", "best gutter installation", "best roof inspection",
        "best emergency roof repair", "best metal roof installation", "best flat roof repair",
        "best roof coating", "best commercial roof repair", "best chimney flashing repair",
        "top rated roof repair", "top rated roof replacement", "top rated roofing contractor",
        "top rated gutter installation", "top rated roof inspection",
        "top rated emergency roof repair", "top rated metal roof installation",
        "top rated flat roof repair", "top rated roof coating",
        "top rated commercial roof repair", "top rated chimney flashing repair",
        "licensed roofing company", "licensed roof repair", "licensed roof replacement",
        "licensed roofing contractor", "licensed gutter installation",
        "licensed roof inspection", "licensed emergency roof repair",
        "licensed metal roof installation", "licensed flat roof repair",
        "licensed roof coating", "licensed commercial roof repair",
        "licensed chimney flashing repair", "certified roofing company",
        "certified roof repair", "certified roof replacement", "certified roofing contractor",
        "certified gutter installation", "certified roof inspection",
        "certified emergency roof repair", "certified metal roof installation",
        "certified flat roof repair", "certified roof coating",
        "certified commercial roof repair", "certified chimney flashing repair",
        "24 hour roofing company", "24 hour roof repair", "24 hour roof replacement",
        "24 hour roofing contractor", "24 hour gutter installation", "24 hour roof inspection",
        "24 hour emergency roof repair", "24 hour metal roof installation",
        "24 hour flat roof repair", "24 hour roof coating", "24 hour commercial roof repair",
        "24 hour chimney flashing repair", "same day roofing company", "same day roof repair",
        "same day roof replacement", "same day roofing contractor",
        "same day gutter installation", "same day roof inspection",
        "same day emergency roof repair", "same day metal roof installation",
        "same day flat roof repair", "same day roof coating",
        "same day commercial roof repair", "same day chimney flashing repair",
        "emergency roofing company", "emergency roof replacement",
        "emergency roofing contractor", "emergency gutter installation",
        "emergency roof inspection", "emergency metal roof installation",
        "emergency flat roof repair", "emergency roof coating",
        "emergency commercial roof repair", "emergency chimney flashing repair",
        "local roof repair", "local roof replacement", "local roofing contractor",
        "local gutter installation", "local roof inspection", "local emergency roof repair",
        "local metal roof installation", "local flat roof repair", "local roof coating",
        "local commercial roof repair", "local chimney flashing repair",
        "family owned roof repair", "family owned roof replacement",
        "family owned roofing contractor", "family owned gutter installation",
        "family owned roof inspection", "family owned emergency roof repair",
        "family owned metal roof installation", "family owned flat roof repair",
        "family owned roof coating", "family owned commercial roof repair",
        "family owned chimney flashing repair", "veteran owned roofing company",
        "veteran owned roof repair", "veteran owned roof replacement",
        "veteran owned roofing contractor", "veteran owned gutter installation",
        "veteran owned roof inspection", "veteran owned emergency roof repair",
        "veteran owned metal roof installation", "veteran owned flat roof repair",
        "veteran owned roof coating", "veteran owned commercial roof repair",
        "veteran owned chimney flashing repair", "trusted roofing company",
        "trusted roof repair", "trusted roof replacement", "trusted roofing contractor",
        "trusted gutter installation", "trusted roof inspection",
        "trusted emergency roof repair", "trusted metal roof installation",
        "trusted flat roof repair", "trusted roof coating", "trusted commercial roof repair",
        "trusted chimney flashing repair", "reliable roofing company", "reliable roof repair",
        "reliable roof replacement", "reliable roofing contractor",
        "reliable gutter installation", "reliable roof inspection",
        "reliable emergency roof repair", "reliable metal roof installation",
        "reliable flat roof repair", "reliable roof coating",
        "reliable commercial roof repair", "reliable chimney flashing repair",
    ],
}

TRADE_LABELS = {
    "hvac": "HVAC", "plumbing": "Plumbing", "roofing": "Roofing",
    "electrical": "Electrical", "landscaping": "Landscaping", "painting": "Painting",
    "cleaning": "Cleaning", "concrete": "Concrete", "pool": "Pool",
    "general_contractor": "General Contractor",
}

FEATURE_WEIGHTS = {
    "local_pack": 0.40, "local_services": 0.20, "organic": 0.30,
    "featured_snippet": 0.05, "ai_overview": 0.03, "people_also_ask": 0.02,
}

TRADE_AVG_TICKET = {
    "hvac": 400, "plumbing": 320, "roofing": 900, "electrical": 350,
    "landscaping": 260, "painting": 320, "cleaning": 180, "pest_control": 210,
    "general_contractor": 2500,
}

TRADE_CPC = {
    "hvac": 45, "plumbing": 35, "roofing": 50, "electrical": 40,
    "landscaping": 15, "painting": 20, "cleaning": 12, "pest_control": 18,
    "general_contractor": 30,
}

TRADE_IMAGES = {
    "hvac":               "https://images.unsplash.com/photo-1621905251189-08b45d6a269e?w=1200&h=440&fit=crop&q=80",
    "plumbing":           "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=1200&h=440&fit=crop&q=80",
    "roofing":            "https://images.unsplash.com/photo-1632207691143-643e2a9a9361?w=1200&h=440&fit=crop&q=80",
    "electrical":         "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1200&h=440&fit=crop&q=80",
    "landscaping":        "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1200&h=440&fit=crop&q=80",
    "painting":           "https://images.unsplash.com/photo-1562259949-e8e7689d7828?w=1200&h=440&fit=crop&q=80",
    "cleaning":           "https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=1200&h=440&fit=crop&q=80",
    "concrete":           "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1200&h=440&fit=crop&q=80",
    "pool":               "https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=1200&h=440&fit=crop&q=80",
    "general_contractor": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=1200&h=440&fit=crop&q=80",
}

FEATURE_LABELS = {
    "local_pack": "Local Pack (3-Map)", "local_services": "Local Services Ads",
    "organic": "Organic Results", "featured_snippet": "Featured Snippet",
    "ai_overview": "AI Overview", "people_also_ask": "People Also Ask", "images": "Image Pack",
}

# ── DataForSEO Client ─────────────────────────────────────────────────────────

def dfs_serp(keyword: str, location: str) -> dict:
    url = "https://api.dataforseo.com/v3/serp/google/organic/live/advanced"
    payload = [{"keyword": keyword, "location_name": location,
                "language_name": "English", "device": "mobile", "depth": 20}]
    resp = requests.post(url, json=payload, auth=(DFS_USER, DFS_PASS), timeout=30)
    resp.raise_for_status()
    data = resp.json()
    if data.get("status_code") != 20000:
        raise ValueError(f"DFS error: {data.get('status_message')}")
    tasks = data.get("tasks", [])
    if not tasks or tasks[0].get("status_code") != 20000:
        return {}
    results = tasks[0].get("result", [])
    return results[0] if results else {}


def dfs_serp_cached(keyword: str, location: str) -> tuple[dict, bool]:
    """Returns (result, from_cache). Checks cache first; fetches and saves if missing or stale."""
    cached = _load_cache(keyword, location)
    if cached is not None:
        return cached, True
    result = dfs_serp(keyword, location)
    _save_cache(keyword, location, result)
    return result, False


_INFORMATIONAL_PATTERNS = [
    r"\bvs\b", r"\bvs\.\b",
    r"^how (to|long|much|often|many)\b",
    r"^when (to|does|do)\b",
    r"^why\b",
    r"^what (causes|is)\b",
    r"^do i need\b",
    r"\bpros and cons\b",
    r"\blifespan\b", r"\blife expectancy\b",
    r"^most reliable\b",
    r"^best .* brand\b",
    r"\bbrands ranked\b",
    r"^how to choose\b", r"^how to lower\b", r"^how to unclog\b",
    r"^signs\b",
    r"^diy\b", r"\btemporary .*fix\b",
]
_INFORMATIONAL_RE = re.compile("|".join(_INFORMATIONAL_PATTERNS), re.IGNORECASE)


def classify_keyword_intent(keyword: str) -> str:
    """
    Tiers a keyword for local SEO targeting:
    'service'       — hire-intent (repair/install/near-me/cost/brand+service/symptom/emergency).
                       Target these directly on money pages (service pages, homepage, location pages).
    'informational' — comparison/research/DIY/lifespan questions with no hire signal.
                       Target these via blog/FAQ content only — they build topical authority,
                       not conversion, and diluting a service page with them hurts relevance.
    """
    return "informational" if _INFORMATIONAL_RE.search(keyword) else "service"


def fetch_keyword_volumes(base_keywords: list, location: str, cache_id: str) -> dict:
    """
    Batch-fetches monthly search volumes from DataForSEO Keywords Data API.
    base_keywords: keyword terms WITHOUT city name (DataForSEO filters by location_name).
    Returns: {keyword: monthly_search_volume}
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = CACHE_DIR / f"__vol__{_cache_key(cache_id, location)}.json"
    if cache_path.exists():
        try:
            data = json.loads(cache_path.read_text(encoding="utf-8"))
            saved_at = datetime.fromisoformat(data["_cached_at"])
            if datetime.now() - saved_at <= timedelta(days=CACHE_TTL_DAYS):
                return data["result"]
        except Exception:
            pass
    url = "https://api.dataforseo.com/v3/keywords_data/google_ads/search_volume/live"
    volumes = {}
    # DataForSEO caps search_volume/live at 1,000 keywords per call — loop in chunks
    # instead of truncating or padding with unrelated keywords.
    for i in range(0, len(base_keywords), 1000):
        chunk = base_keywords[i:i + 1000]
        payload = [{"keywords": chunk, "location_name": location, "language_name": "English"}]
        resp = requests.post(url, json=payload, auth=(DFS_USER, DFS_PASS), timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if data.get("status_code") == 20000:
            tasks = data.get("tasks", [])
            if tasks and tasks[0].get("status_code") == 20000:
                for r in (tasks[0].get("result", []) or []):
                    kw = r.get("keyword", "")
                    sv = r.get("search_volume") or 0
                    volumes[kw] = sv
    cache_path.write_text(json.dumps({"_cached_at": datetime.now().isoformat(), "result": volumes},
                                      ensure_ascii=False), encoding="utf-8")
    return volumes


def calc_revenue_opportunity(volumes: dict, trade: str) -> dict:
    """Estimate monthly revenue potential for the top local pack position."""
    total_searches = sum(volumes.values())
    avg_ticket = TRADE_AVG_TICKET.get(trade, 350)
    cpc = TRADE_CPC.get(trade, 30)
    # One of three map-pack spots: ~12% CTR share; 8% of those call/fill form; 40% close
    clicks = round(total_searches * 0.12)
    leads = round(clicks * 0.08)
    jobs = round(leads * 0.40)
    revenue = jobs * avg_ticket
    # High-end: 15% CTR, 10% lead, 50% close
    revenue_high = round(total_searches * 0.15 * 0.10 * 0.50 * avg_ticket)
    # PPC equivalent: what it would cost to buy these clicks via Google Ads (avg 3% paid CTR)
    ppc_monthly = round(total_searches * 0.03 * cpc)
    return {
        "total_searches": total_searches,
        "avg_ticket": avg_ticket,
        "cpc": cpc,
        "clicks": clicks,
        "leads": leads,
        "jobs": jobs,
        "revenue": revenue,
        "revenue_high": max(revenue, revenue_high),
        "ppc_monthly": ppc_monthly,
    }

# ── Feature Parser ────────────────────────────────────────────────────────────

def parse_features(serp_result: dict, domain: str | None) -> dict:
    items = serp_result.get("items", []) or []
    f = {k: {"fired": False, "businesses": [], "client_present": False}
         for k in ["local_pack", "local_services", "featured_snippet", "ai_overview"]}
    f["organic"] = {"fired": False, "positions": [], "client_present": False, "client_rank": None}
    f["people_also_ask"] = {"fired": False, "questions": []}
    f["images"] = {"fired": False}

    for item in items:
        t = item.get("type", "")
        if t == "local_pack":
            f["local_pack"]["fired"] = True
            name = item.get("title", "")
            url = item.get("url", "") or ""
            domain_val = item.get("domain", "") or ""
            rating_obj = item.get("rating") or {}
            f["local_pack"]["businesses"].append({
                "name": name, "url": url, "domain": domain_val,
                "phone": item.get("phone", "") or "",
                "rating": rating_obj.get("value"),
                "reviews": rating_obj.get("votes_count"),
                "slot": item.get("rank_group", 0),
            })
            if domain and (domain.lower() in url.lower() or domain.lower() in domain_val.lower()):
                f["local_pack"]["client_present"] = True
        elif t == "local_services":
            f["local_services"]["fired"] = True
            for svc in (item.get("items") or []):
                name = svc.get("title", "") or svc.get("domain", "")
                f["local_services"]["businesses"].append({"name": name})
                if domain and domain.lower() in (svc.get("url", "") or "").lower():
                    f["local_services"]["client_present"] = True
        elif t == "organic":
            f["organic"]["fired"] = True
            rank = item.get("rank_absolute", 0)
            url = item.get("url", "") or ""
            d = item.get("domain", "") or ""
            f["organic"]["positions"].append({"rank": rank, "domain": d})
            if domain and (domain.lower() in url.lower() or domain.lower() in d.lower()):
                f["organic"]["client_present"] = True
                if f["organic"]["client_rank"] is None:
                    f["organic"]["client_rank"] = rank
        elif t == "featured_snippet":
            f["featured_snippet"]["fired"] = True
            url = item.get("url", "") or ""
            if domain and domain.lower() in url.lower():
                f["featured_snippet"]["client_present"] = True
        elif t == "ai_overview":
            f["ai_overview"]["fired"] = True
            for src in (item.get("sources") or item.get("items") or []):
                if domain and domain.lower() in (src.get("url", "") or "").lower():
                    f["ai_overview"]["client_present"] = True
        elif t == "people_also_ask":
            f["people_also_ask"]["fired"] = True
            for q in (item.get("items") or []):
                f["people_also_ask"]["questions"].append(q.get("title", ""))
        elif t == "images":
            f["images"]["fired"] = True
    return f

# ── Aggregators ───────────────────────────────────────────────────────────────

def aggregate_competitors(all_features: list) -> list:
    counts: dict[str, int] = {}
    profiles: dict[str, dict] = {}
    for kw_f in all_features:
        for biz in kw_f.get("local_pack", {}).get("businesses", []):
            name = biz.get("name", "").strip()
            if not name:
                continue
            counts[name] = counts.get(name, 0) + 1
            if name not in profiles:
                profiles[name] = {
                    "phone": biz.get("phone", "") or "",
                    "domain": biz.get("domain", "") or "",
                    "rating": biz.get("rating"),
                    "reviews": biz.get("reviews"),
                }
            else:
                # Keep the highest review count seen (most authoritative snapshot)
                if biz.get("reviews") and (not profiles[name]["reviews"] or
                        biz["reviews"] > profiles[name]["reviews"]):
                    profiles[name]["reviews"] = biz["reviews"]
                    profiles[name]["rating"] = biz.get("rating")
                if not profiles[name]["phone"] and biz.get("phone"):
                    profiles[name]["phone"] = biz["phone"]
    total = len(all_features)
    ranked = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return [{
        "name": n, "appearances": c,
        "prevalence_pct": round(c / total * 100) if total else 0,
        **profiles.get(n, {}),
    } for n, c in ranked[:15]]

def aggregate_position_spread(all_features: list) -> dict:
    """Returns {name: {1: count, 2: count, 3: count}} tracking map pack slot distribution."""
    spread: dict[str, dict] = {}
    for kw_f in all_features:
        for biz in kw_f.get("local_pack", {}).get("businesses", []):
            name = biz.get("name", "").strip()
            if not name:
                continue
            slot = biz.get("slot", 0)
            if name not in spread:
                spread[name] = {1: 0, 2: 0, 3: 0}
            if slot in (1, 2, 3):
                spread[name][slot] += 1
    return spread


def build_opportunity_data(keywords: list, volumes: dict, all_features: list,
                           market_leader: str) -> list:
    """
    Returns up to 6 opportunity keywords — sorted by open + high volume first.
    'Open' = market leader does NOT hold slot 1 for that specific keyword.
    """
    rows = []
    for i, kw in enumerate(keywords):
        if i >= len(all_features):
            break
        businesses = all_features[i].get("local_pack", {}).get("businesses", [])
        vol = volumes.get(kw, 0)
        slot1_biz = next((b["name"] for b in businesses if b.get("slot") == 1), None)
        leader_holds_slot1 = bool(slot1_biz and slot1_biz.strip() == market_leader.strip())
        rows.append({
            "keyword": kw,
            "volume": vol,
            "slot1": slot1_biz or "—",
            "is_open": not leader_holds_slot1 and bool(businesses),
        })
    # Open opportunities first, then by volume descending
    rows.sort(key=lambda r: (not r["is_open"], -r["volume"]))
    return rows[:6]


def aggregate_stats(all_features: list) -> dict:
    total = len(all_features)
    stats = {}
    for feat in ["local_pack", "local_services", "organic", "featured_snippet",
                 "ai_overview", "people_also_ask", "images"]:
        fired = sum(1 for f in all_features if f.get(feat, {}).get("fired"))
        stats[feat] = {"fired_count": fired,
                       "prevalence_pct": round(fired / total * 100) if total else 0}
    questions = []
    for f in all_features:
        questions.extend(f.get("people_also_ask", {}).get("questions", []))
    stats["paa_questions"] = list(dict.fromkeys(questions))[:8]
    return stats

def calc_ownership_score(all_features: list, domain: str | None) -> dict:
    total = len(all_features)
    if not total:
        return {"client": 0.0, "competitors": {}}
    client_pts = 0.0
    comp_pts: dict[str, float] = {}
    for kw_f in all_features:
        lp = kw_f.get("local_pack", {})
        if domain:
            if lp.get("client_present"):
                client_pts += FEATURE_WEIGHTS["local_pack"]
            if kw_f.get("local_services", {}).get("client_present"):
                client_pts += FEATURE_WEIGHTS["local_services"]
            if kw_f.get("organic", {}).get("client_present"):
                client_pts += FEATURE_WEIGHTS["organic"]
            if kw_f.get("featured_snippet", {}).get("client_present"):
                client_pts += FEATURE_WEIGHTS["featured_snippet"]
            if kw_f.get("ai_overview", {}).get("client_present"):
                client_pts += FEATURE_WEIGHTS["ai_overview"]
        for biz in lp.get("businesses", []):
            name = biz.get("name", "").strip()
            if name:
                comp_pts[name] = comp_pts.get(name, 0.0) + FEATURE_WEIGHTS["local_pack"]
    max_pts = sum(FEATURE_WEIGHTS.values()) * total
    client_score = round(client_pts / max_pts * 100, 1) if max_pts else 0.0
    comp_scores = {n: round(p / max_pts * 100, 1) for n, p in comp_pts.items()}
    top_competitors = dict(sorted(comp_scores.items(), key=lambda x: x[1], reverse=True)[:15])
    return {"client": client_score, "competitors": top_competitors}

# ── HTML Helpers ─────────────────────────────────────────────────────────────

def _build_position_spread_html(spread: dict, competitors: list, total_kw: int) -> str:
    """Stacked bar per competitor showing slot 1/2/3 distribution across all keywords."""
    rows = ""
    for comp in competitors[:15]:
        name = comp["name"]
        d = spread.get(name, {1: 0, 2: 0, 3: 0})
        s1, s2, s3 = d.get(1, 0), d.get(2, 0), d.get(3, 0)
        total = s1 + s2 + s3
        if not total:
            continue
        w1 = round(s1 / total_kw * 100)
        w2 = round(s2 / total_kw * 100)
        w3 = round(s3 / total_kw * 100)
        name_short = name[:38] + ("…" if len(name) > 38 else "")
        rows += f"""
        <div class="spread-row">
          <div class="spread-name">{name_short}</div>
          <div class="spread-bar-wrap">
            <div class="spread-seg s1" style="width:{w1}%" title="Slot 1: {s1} of {total_kw} searches"></div>
            <div class="spread-seg s2" style="width:{w2}%" title="Slot 2: {s2} of {total_kw} searches"></div>
            <div class="spread-seg s3" style="width:{w3}%" title="Slot 3: {s3} of {total_kw} searches"></div>
          </div>
          <div class="spread-tally"><span class="spread-slot-1">{s1}×&nbsp;#1</span>&ensp;{s2}×&nbsp;#2&ensp;{s3}×&nbsp;#3</div>
        </div>"""
    legend = """
    <div class="spread-legend">
      <span class="spread-dot s1"></span> Slot 1 &mdash; top of map (most clicks)
      &ensp;<span class="spread-dot s2"></span> Slot 2
      &ensp;<span class="spread-dot s3"></span> Slot 3
    </div>"""
    return rows + legend


def _build_opportunity_rows(opp_data: list) -> str:
    rows = ""
    for row in opp_data:
        vol = f"{row['volume']:,}/mo" if row["volume"] else "—"
        badge_cls = "opp-open" if row["is_open"] else "opp-taken"
        badge_label = "Winnable" if row["is_open"] else "Leader owns it"
        holder = row["slot1"]
        if len(holder) > 32:
            holder = holder[:32] + "…"
        rows += f"""
        <tr>
          <td class="opp-kw">{row['keyword']}</td>
          <td class="opp-vol">{vol}</td>
          <td class="opp-holder">{holder}</td>
          <td><span class="opp-badge {badge_cls}">{badge_label}</span></td>
        </tr>"""
    return rows


def _build_kw_rows(keywords: list, volumes: dict, stats: dict) -> str:
    """Build keyword table rows sorted by search volume descending."""
    lp_fired_count = stats.get("local_pack", {}).get("fired_count", 0)
    total_kw = len(keywords)
    # Approximate per-keyword LP rate — use aggregate for all rows since we don't track per-kw
    rows = ""
    for kw in sorted(keywords, key=lambda k: volumes.get(k, 0), reverse=True):
        vol = volumes.get(kw, 0)
        vol_str = f"{vol:,}" if vol else "—"
        lp_class = "yes" if lp_fired_count / total_kw >= 0.5 else "no"
        lp_label = "Yes" if lp_fired_count / total_kw >= 0.5 else "Varies"
        rows += f"""
        <tr>
          <td>{kw}</td>
          <td class="kw-vol">{vol_str}/mo</td>
          <td><span class="kw-badge {lp_class}">{lp_label}</span></td>
        </tr>"""
    return rows

# ── HTML Generator ────────────────────────────────────────────────────────────

def build_feature_rows(stats: dict, domain: str | None) -> str:
    rows = ""
    features = [
        ("local_pack", "🗺️"), ("local_services", "📋"), ("organic", "🔗"),
        ("featured_snippet", "⭐"), ("ai_overview", "🤖"), ("people_also_ask", "❓"), ("images", "🖼️"),
    ]
    for feat, icon in features:
        label = FEATURE_LABELS.get(feat, feat)
        pct = stats.get(feat, {}).get("prevalence_pct", 0)
        bar_w = pct
        severity = "gap" if pct >= 50 else "low"
        rows += f"""
        <tr>
          <td class="feat-name">{icon} {label}</td>
          <td class="feat-pct">
            <div class="bar-wrap"><div class="bar-fill {severity}" style="width:{bar_w}%"></div></div>
            <span class="pct-label">{pct}% of searches</span>
          </td>
          <td class="feat-client">{"—" if not domain else ("✅ Present" if stats.get(feat, {}).get("fired_count", 0) > 0 else "❌ Missing")}</td>
        </tr>"""
    return rows

def build_competitor_bars(competitors: list, client_score: float, domain: str | None) -> str:
    all_items = []
    if domain:
        all_items.append(("Your Business", client_score, "client"))
    for c in competitors:
        all_items.append((c["name"], c["prevalence_pct"] * 0.4, "competitor"))
    max_score = max((s for _, s, _ in all_items), default=1) or 1
    bars = ""
    for name, score, kind in all_items:
        w = round(score / max_score * 100)
        cls = "bar-client" if kind == "client" else "bar-comp"
        bars += f"""
        <div class="comp-row">
          <div class="comp-name">{name}</div>
          <div class="comp-bar-wrap">
            <div class="comp-bar {cls}" style="width:{w}%"></div>
            <span class="comp-score">{score:.1f}</span>
          </div>
        </div>"""
    return bars

def generate_html(trade: str, city: str, state: str, year: int, domain: str | None,
                  keywords: list, stats: dict, competitors: list, ownership: dict,
                  volumes: dict | None = None, all_features: list | None = None,
                  trade_image: str = "") -> str:
    tl = TRADE_LABELS.get(trade, trade.replace("_", " ").title())
    city_t = city.title()
    st = state.upper()
    total_kw = len(keywords)
    lp_pct = stats.get("local_pack", {}).get("prevalence_pct", 0)
    lp_fired = stats.get("local_pack", {}).get("fired_count", 0)
    lsa_pct = stats.get("local_services", {}).get("prevalence_pct", 0)
    ai_pct = stats.get("ai_overview", {}).get("prevalence_pct", 0)
    client_score = ownership.get("client", 0.0)
    comp_scores = ownership.get("competitors", {})
    top_name = list(comp_scores.keys())[0] if comp_scores else "Top Competitor"
    top_name_short = top_name.split("–")[0].split("-")[0].strip()[:30]
    top_appearances = competitors[0]["appearances"] if competitors else 0
    mode_label = f"Your site ({domain})" if domain else "No website detected"
    # Revenue opportunity
    rev = calc_revenue_opportunity(volumes or {}, trade)
    total_searches = rev["total_searches"]
    vol_display = f"{total_searches:,}" if total_searches else "—"
    rev_display = f"${rev['revenue_high']:,}" if rev["revenue_high"] else "—"
    ppc_display = f"${rev['ppc_monthly']:,}" if rev.get("ppc_monthly") else "—"
    hero_sub = (
        f"We tracked {total_kw} real Google searches for {tl} in {city_t} this month. "
        f"Here's what your customers see — and which competitors are capturing them."
    )
    now = datetime.now()
    month = now.strftime("%B %Y")
    data_date = now.strftime("%B %d, %Y")
    # Competitor profile card
    top_comp = competitors[0] if competitors else {}
    top_rating = top_comp.get("rating")
    top_reviews = top_comp.get("reviews")
    top_phone = top_comp.get("phone", "")
    top_domain = top_comp.get("domain", "")
    stars_html = ""
    if top_rating:
        full = int(top_rating)
        half = 1 if (top_rating - full) >= 0.5 else 0
        stars_html = "★" * full + ("½" if half else "") + "☆" * (5 - full - half)
    # NOTE: FAQPage schema was previously auto-generated here with a hardcoded
    # non-answer ("This is a common question Dallas {tl} customers ask...") that
    # also leaked the literal word "Dallas" into every report regardless of city.
    # Real FAQ answers require manual research per report and are not auto-generated.
    # If a report needs FAQPage schema, write real per-question answers by hand
    # and add the schema block directly in that report's HTML.
    # Position spread + opportunity analysis
    _af = all_features or []
    spread = aggregate_position_spread(_af)
    spread_html = _build_position_spread_html(spread, competitors, total_kw)
    opp_data = build_opportunity_data(keywords, volumes or {}, _af, top_name)
    opp_rows = _build_opportunity_rows(opp_data)
    open_count = sum(1 for r in opp_data if r["is_open"])
    # Slot 1 count for market leader (for insight headline)
    leader_s1 = spread.get(top_name, {}).get(1, 0)
    feat_rows = build_feature_rows(stats, domain)
    comp_bars = build_competitor_bars(competitors, client_score, domain)
    paa_q = stats.get("paa_questions", [])
    paa_html = "".join(f"<li>{q}</li>" for q in paa_q[:6]) if paa_q else "<li>No PAA data captured.</li>"
    gap_items = []
    if lp_pct >= 50 and (not domain or client_score < 10):
        gap_items.append(("Local Pack", f"Fires on {lp_pct}% of searches. This is the most clicked result in local markets.", "critical"))
    if lsa_pct >= 20:
        gap_items.append(("Local Services Ads", f"Fires on {lsa_pct}% of searches — above everything including organic. Google-guaranteed badge.", "critical"))
    if ai_pct >= 20:
        gap_items.append(("AI Overview", f"Fires on {ai_pct}% of searches. Google answers the question for the user — if you're not cited, a competitor is.", "moderate"))
    gap_items.append(("People Also Ask", "Surfaces on 90%+ of local searches. Every question Google shows is a content gap your site could own.", "moderate"))
    gap_html = ""
    for title, desc, severity in gap_items:
        icon = "🔴" if severity == "critical" else "🟠"
        gap_html += f"""
        <div class="gap-card {severity}">
          <div class="gap-title">{icon} {title}</div>
          <p class="gap-desc">{desc}</p>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{city_t} {tl} SEO Report {year} | Map Pack Rankings</title>
<meta name="description" content="We analyzed {total_kw} Google searches for {tl} in {city_t}, {st}: who owns the map pack and what it's costing you. {data_date} data.">
<link rel="canonical" href="https://copperbuilds.com/reports/{trade.replace('_','-')}-seo-report-{city.replace(' ','-').lower()}-{state.lower()}-{year}/">
<meta property="og:type" content="article">
<meta property="og:site_name" content="CopperBuilds">
<meta property="og:title" content="{city_t} {tl} SEO Report {year}: Map Pack Rankings">
<meta property="og:description" content="We analyzed {total_kw} Google searches for {tl} in {city_t}, {st}: who owns the map pack and what it's costing you.">
<meta property="og:url" content="https://copperbuilds.com/reports/{trade.replace('_','-')}-seo-report-{city.replace(' ','-').lower()}-{state.lower()}-{year}/">
<meta property="og:image" content="https://copperbuilds.com/brand_assets/brand-kit/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{city_t} {tl} SEO Report {year}: Map Pack Rankings">
<meta name="twitter:description" content="We analyzed {total_kw} Google searches for {tl} in {city_t}, {st}: who owns the map pack and what it's costing you.">
<meta name="twitter:image" content="https://copperbuilds.com/brand_assets/brand-kit/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Calistoga&family=DM+Sans:wght@400;500;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Organization",
      "@id": "https://copperbuilds.com/#organization",
      "name": "CopperBuilds",
      "url": "https://copperbuilds.com",
      "logo": "https://copperbuilds.com/brand_assets/logo.svg",
      "contactPoint": {{"@type": "ContactPoint", "email": "luis.copperbuilds@gmail.com", "contactType": "customer service"}}
    }},
    {{
      "@type": "Article",
      "headline": "{city_t} {tl} SEO Report {year} — Who's Winning Google in {city_t}, {st}",
      "description": "We analyzed {total_kw} live Google searches for {tl} in {city_t}, {st}. See who owns the map pack, keyword search volumes, and estimated monthly revenue.",
      "datePublished": "{now.strftime('%Y-%m-%d')}",
      "dateModified": "{now.strftime('%Y-%m-%d')}",
      "author": {{"@type": "Organization", "name": "CopperBuilds", "url": "https://copperbuilds.com"}},
      "publisher": {{"@type": "Organization", "name": "CopperBuilds", "logo": {{"@type": "ImageObject", "url": "https://copperbuilds.com/brand_assets/logo.svg"}}}}
    }},
    {{"@type": "WebPage"}},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://copperbuilds.com/"}},
        {{"@type": "ListItem", "position": 2, "name": "Reports", "item": "https://copperbuilds.com/reports/"}},
        {{"@type": "ListItem", "position": 3, "name": "{city_t} {tl} SERP Report {year}", "item": "https://copperbuilds.com/reports/{trade.replace('_','-')}-seo-report-{city.replace(' ','-').lower()}-{state.lower()}-{year}/"}}
      ]
    }}
  ]
}}
</script>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#FAFAF7;--surface:#fff;--elevated:#F5F0EA;
  --copper:#B87333;--copper-dim:#B8733318;--copper-hover:#96602A;
  --accent:#B87333;--accent-hover:#9A6129;--accent-dim:rgba(184,115,51,0.08);--accent-border:rgba(184,115,51,0.22);
  --teal:#4E9F7D;--teal-dim:#4E9F7D18;
  --ink:#1C1917;--muted:#78716C;--warm-stone:#6B6560;--subtle:#A8A29E;
  --border:#E7E0D8;--rule:#1C191714;--container-max:1200px;
  --r-sm:4px;--r-md:6px;--r-lg:12px;--r-xl:20px;--r-pill:100px;
}}
body{{font-family:'DM Sans',sans-serif;background:var(--bg);color:var(--ink);line-height:1.72;font-size:1rem}}
a{{color:var(--copper);text-decoration:none}}
a:hover{{color:var(--copper-hover)}}

.container{{max-width:var(--container-max);margin:0 auto;padding:0 2rem}}
.rule{{border:none;border-top:1px solid var(--rule)}}
.footer-grid{{display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr;gap:3rem;margin-bottom:3rem}}
@media(max-width:900px){{.footer-grid{{grid-template-columns:1fr 1fr;gap:2rem}}}}
@media(max-width:540px){{.footer-grid{{grid-template-columns:1fr}}.container{{padding:0 1.5rem}}}}

/* NAV injected by /js/nav.js */
.btn{{display:inline-block;text-decoration:none;transition:background .2s}}
.btn-primary{{background:var(--copper);color:#fff;padding:10px 22px;border-radius:var(--r-md);font-family:'JetBrains Mono',monospace;font-size:.7rem;font-weight:500;letter-spacing:.08em;text-transform:uppercase;cursor:pointer}}
.btn-primary:hover{{background:var(--copper-hover);color:#fff}}
.btn-teal{{background:var(--teal);color:#fff;padding:14px 32px;border-radius:var(--r-md);font-family:'JetBrains Mono',monospace;font-size:.78rem;font-weight:500;letter-spacing:.08em;text-transform:uppercase;border:none;cursor:pointer;transition:background .2s;display:inline-block}}
.btn-teal:hover{{background:#3D8B6C;color:#fff}}

/* HERO */
.hero{{padding:72px 40px 64px;max-width:1000px;margin:0 auto}}
.tag-pill{{display:inline-block;background:var(--copper-dim);color:var(--copper);padding:5px 14px;border-radius:var(--r-pill);font-family:'JetBrains Mono',monospace;font-size:.68rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;margin-bottom:24px}}
.hero h1{{font-family:'Calistoga',serif;font-size:clamp(2rem,4.5vw,3.2rem);line-height:1.1;color:var(--ink);margin-bottom:20px;max-width:800px}}
.hero-sub{{font-size:1.1rem;color:var(--muted);max-width:620px;margin-bottom:48px;line-height:1.65}}
.stat-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px;margin-bottom:0}}
.stat-card{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-lg);padding:24px;}}
.stat-num{{font-family:'JetBrains Mono',monospace;font-size:2rem;font-weight:500;color:var(--copper);line-height:1}}
.stat-num.teal{{color:var(--teal)}}
.stat-num.danger{{color:#C53030}}
.stat-label{{font-size:.82rem;color:var(--muted);margin-top:6px;line-height:1.4}}

/* SECTIONS */
.section{{padding:64px 40px;max-width:1000px;margin:0 auto}}
.section-divider{{border:none;border-top:1px solid var(--border);margin:0}}
.section-tag{{font-family:'JetBrains Mono',monospace;font-size:.68rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--copper);margin-bottom:12px}}
.section h2{{font-family:'Calistoga',serif;font-size:clamp(1.6rem,3vw,2.2rem);line-height:1.15;margin-bottom:12px}}
.section-sub{{color:var(--muted);font-size:.95rem;margin-bottom:36px;max-width:600px}}

/* FEATURE TABLE */
.feat-table{{width:100%;border-collapse:collapse}}
.feat-table th{{text-align:left;font-family:'JetBrains Mono',monospace;font-size:.65rem;letter-spacing:.1em;text-transform:uppercase;color:var(--subtle);padding:10px 0;border-bottom:1px solid var(--border)}}
.feat-table td{{padding:14px 0;border-bottom:1px solid var(--rule);vertical-align:middle}}
.feat-name{{font-size:.95rem;font-weight:500;white-space:nowrap;padding-right:24px;width:220px}}
.feat-pct{{min-width:240px}}
.bar-wrap{{height:6px;background:var(--border);border-radius:3px;overflow:hidden;width:100%;max-width:200px;display:inline-block;vertical-align:middle;margin-right:10px}}
.bar-fill{{height:100%;border-radius:3px;transition:width .4s}}
.bar-fill.gap{{background:var(--copper)}}
.bar-fill.low{{background:var(--border)}}
.pct-label{{font-family:'JetBrains Mono',monospace;font-size:.72rem;color:var(--muted);vertical-align:middle}}
.feat-client{{font-size:.88rem;white-space:nowrap;padding-left:16px}}

/* COMPETITOR BARS */
.comp-row{{margin-bottom:16px}}
.comp-name{{font-size:.88rem;font-weight:500;margin-bottom:6px;color:var(--ink)}}
.comp-bar-wrap{{display:flex;align-items:center;gap:10px}}
.comp-bar{{height:10px;border-radius:5px;transition:width .4s;min-width:4px}}
.bar-client{{background:var(--teal)}}
.bar-comp{{background:var(--copper)}}
.comp-score{{font-family:'JetBrains Mono',monospace;font-size:.72rem;color:var(--muted)}}

/* GAP CARDS */
.gap-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}}
.gap-card{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r-lg);padding:24px}}
.gap-card.critical{{border-left:3px solid #C53030}}
.gap-card.moderate{{border-left:3px solid var(--copper)}}
.gap-title{{font-weight:700;font-size:.95rem;margin-bottom:8px}}
.gap-desc{{font-size:.88rem;color:var(--muted);line-height:1.6}}

/* PAA */
.paa-list{{list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:10px}}
.paa-list li{{background:var(--elevated);border-radius:var(--r-md);padding:12px 16px;font-size:.88rem;color:var(--ink)}}

/* DATA NOTE */
.data-note{{font-size:.76rem;color:var(--subtle);margin-top:20px;font-style:italic;line-height:1.5}}

/* CONSUMER BEHAVIOR CALLOUT */
.stat-hook{{background:var(--ink);border-radius:var(--r-xl);padding:40px;margin:0 40px 0;max-width:calc(1000px - 80px);margin-left:auto;margin-right:auto}}
.stat-hook-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}
.hook-stat{{text-align:center}}
.hook-num{{font-family:'JetBrains Mono',monospace;font-size:2.2rem;font-weight:500;color:var(--copper);line-height:1}}
.hook-label{{font-size:.82rem;color:rgba(255,255,255,0.6);margin-top:6px;line-height:1.4}}

/* KEYWORDS TABLE */
.kw-table{{width:100%;border-collapse:collapse;margin-top:0}}
.kw-table th{{text-align:left;font-family:'JetBrains Mono',monospace;font-size:.65rem;letter-spacing:.1em;text-transform:uppercase;color:var(--subtle);padding:10px 0;border-bottom:1px solid var(--border)}}
.kw-table td{{padding:12px 0;border-bottom:1px solid var(--rule);font-size:.9rem;vertical-align:middle}}
.kw-vol{{font-family:'JetBrains Mono',monospace;font-size:.82rem;color:var(--copper);font-weight:500}}
.kw-badge{{display:inline-block;font-size:.65rem;font-family:'JetBrains Mono',monospace;padding:2px 8px;border-radius:var(--r-pill);font-weight:500}}
.kw-badge.yes{{background:var(--teal-dim);color:var(--teal)}}
.kw-badge.no{{background:var(--copper-dim);color:var(--copper)}}
.kw-total-row{{font-size:.82rem;color:var(--muted);margin-top:12px;font-style:italic}}

/* COMPETITOR PROFILE CARD */
.leader-card{{background:var(--surface);border:2px solid var(--copper);border-radius:var(--r-xl);padding:32px;margin-bottom:32px;display:grid;grid-template-columns:1fr auto;gap:24px;align-items:start}}
.leader-badge{{display:inline-block;background:var(--copper-dim);color:var(--copper);font-family:'JetBrains Mono',monospace;font-size:.65rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;padding:4px 12px;border-radius:var(--r-pill);margin-bottom:12px}}
.leader-name{{font-family:'Calistoga',serif;font-size:1.4rem;color:var(--ink);margin-bottom:8px;line-height:1.2}}
.leader-meta{{display:flex;flex-wrap:wrap;gap:16px;margin-top:12px}}
.leader-meta-item{{font-size:.85rem;color:var(--muted);display:flex;align-items:center;gap:6px}}
.leader-meta-item strong{{color:var(--ink)}}
.leader-stars{{color:#D97706;font-size:1rem;letter-spacing:1px}}
.leader-stat{{text-align:right}}
.leader-stat-num{{font-family:'JetBrains Mono',monospace;font-size:2rem;font-weight:500;color:var(--copper)}}
.leader-stat-label{{font-size:.78rem;color:var(--muted);margin-top:4px;line-height:1.4}}
@media(max-width:640px){{.leader-card{{grid-template-columns:1fr}}.stat-hook-grid{{grid-template-columns:1fr}}.stat-hook{{margin:0 20px}}}}

/* PPC CALLOUT */
.ppc-callout{{background:var(--elevated);border:1px solid var(--border);border-radius:var(--r-lg);padding:24px;margin-top:24px;display:flex;align-items:center;gap:24px;flex-wrap:wrap}}
.ppc-num{{font-family:'JetBrains Mono',monospace;font-size:1.6rem;font-weight:500;color:var(--copper);white-space:nowrap}}
.ppc-label{{font-size:.88rem;color:var(--muted);line-height:1.5}}

/* INTERNAL LINKS */
.internal-links{{margin-top:24px;display:flex;flex-wrap:wrap;gap:10px}}
.internal-link{{display:inline-block;border:1px solid var(--border);border-radius:var(--r-md);padding:8px 16px;font-size:.82rem;color:var(--copper);transition:border-color .2s,background .2s}}
.internal-link:hover{{background:var(--copper-dim);border-color:var(--copper);color:var(--copper)}}

/* TIMELINE NOTE */
.timeline-note{{font-size:.85rem;color:var(--muted);margin-top:12px;display:flex;align-items:center;gap:8px}}

/* POSITION SPREAD */
.spread-row{{margin-bottom:20px}}
.spread-name{{font-size:.88rem;font-weight:500;color:var(--ink);margin-bottom:7px}}
.spread-bar-wrap{{display:flex;height:12px;border-radius:6px;overflow:hidden;background:var(--border);gap:1px}}
.spread-seg{{height:100%;transition:width .4s;min-width:0}}
.spread-seg.s1{{background:var(--copper)}}
.spread-seg.s2{{background:var(--teal)}}
.spread-seg.s3{{background:var(--subtle)}}
.spread-tally{{font-family:'JetBrains Mono',monospace;font-size:.72rem;color:var(--muted);margin-top:5px}}
.spread-slot-1{{color:var(--copper);font-weight:600}}
.spread-legend{{display:flex;gap:6px;margin-top:20px;font-size:.78rem;color:var(--muted);align-items:center;flex-wrap:wrap}}
.spread-dot{{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:3px;vertical-align:middle}}
.spread-dot.s1{{background:var(--copper)}}
.spread-dot.s2{{background:var(--teal)}}
.spread-dot.s3{{background:var(--subtle)}}
.spread-insight{{background:var(--copper-dim);border-left:3px solid var(--copper);border-radius:0 var(--r-md) var(--r-md) 0;padding:14px 18px;margin-bottom:28px;font-size:.9rem;color:var(--ink);line-height:1.55}}
.spread-insight strong{{color:var(--copper)}}

/* OPPORTUNITY TABLE */
.opp-table{{width:100%;border-collapse:collapse}}
.opp-table th{{text-align:left;font-family:'JetBrains Mono',monospace;font-size:.65rem;letter-spacing:.1em;text-transform:uppercase;color:var(--subtle);padding:10px 0;border-bottom:1px solid var(--border)}}
.opp-table td{{padding:13px 0;border-bottom:1px solid var(--rule);vertical-align:middle}}
.opp-kw{{font-size:.9rem;font-weight:500;padding-right:16px}}
.opp-vol{{font-family:'JetBrains Mono',monospace;font-size:.82rem;color:var(--copper);font-weight:500;white-space:nowrap;padding-right:16px}}
.opp-holder{{font-size:.82rem;color:var(--muted);padding-right:16px}}
.opp-badge{{display:inline-block;font-size:.65rem;font-family:'JetBrains Mono',monospace;padding:3px 9px;border-radius:var(--r-pill);font-weight:500;letter-spacing:.05em}}
.opp-badge.opp-open{{background:#D1FAE5;color:#065F46}}
.opp-badge.opp-taken{{background:var(--copper-dim);color:var(--copper)}}
.opp-note{{font-size:.76rem;color:var(--subtle);margin-top:14px;font-style:italic;line-height:1.55}}

/* REVENUE SECTION */
.rev-section{{padding:64px 40px;max-width:1000px;margin:0 auto}}
.rev-banner{{background:var(--ink);color:#fff;border-radius:var(--r-xl);padding:48px;margin-bottom:32px}}
.rev-banner .section-tag{{color:var(--copper)}}
.rev-banner h2{{font-family:'Calistoga',serif;font-size:clamp(1.6rem,3vw,2.2rem);line-height:1.15;margin-bottom:8px;color:#fff}}
.rev-banner p{{color:rgba(255,255,255,0.6);font-size:.95rem;margin-bottom:0;max-width:580px}}
.rev-steps{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin-top:32px}}
.rev-step{{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:var(--r-lg);padding:20px}}
.rev-step-num{{font-family:'JetBrains Mono',monospace;font-size:1.4rem;font-weight:500;color:var(--copper);line-height:1;margin-bottom:6px}}
.rev-step-label{{font-size:.78rem;color:rgba(255,255,255,0.5);line-height:1.4}}
.rev-step-formula{{font-size:.72rem;color:rgba(255,255,255,0.35);margin-top:4px;font-style:italic}}
.rev-total{{background:var(--copper);border-radius:var(--r-lg);padding:20px}}
.rev-total .rev-step-num{{color:#fff;font-size:1.6rem}}
.rev-total .rev-step-label{{color:rgba(255,255,255,0.8)}}
.rev-disclaimer{{font-size:.76rem;color:var(--subtle);margin-top:16px;font-style:italic}}

/* PITCH */
.pitch{{background:var(--elevated);border-radius:var(--r-xl);padding:56px 48px;margin:0 auto;max-width:820px}}
.pitch h2{{font-family:'Calistoga',serif;font-size:clamp(1.5rem,2.5vw,2rem);margin-bottom:20px;line-height:1.2}}
.pitch p{{color:var(--muted);margin-bottom:16px;font-size:1rem;max-width:620px}}

/* CTA */
.cta-block{{text-align:center;padding:80px 40px}}
.cta-block h2{{font-family:'Calistoga',serif;font-size:clamp(1.8rem,3.5vw,2.6rem);margin-bottom:16px;max-width:600px;margin-left:auto;margin-right:auto;line-height:1.15}}
.cta-block p{{color:var(--muted);margin-bottom:36px;font-size:1rem}}
.cta-secondary{{display:block;margin-top:16px;font-size:.85rem;color:var(--muted)}}


@media(max-width:640px){{
  .nav{{padding:16px 20px}}
  .hero,.section{{padding-left:20px;padding-right:20px}}
  .pitch{{padding:36px 24px}}
  .footer{{padding:24px 20px;flex-direction:column;align-items:flex-start}}
  .stat-grid{{grid-template-columns:1fr 1fr}}
  .table-scroll{{overflow-x:auto;-webkit-overflow-scrolling:touch}}
  .feat-table{{min-width:520px}}
  .cta-block{{padding:56px 20px}}
}}
@media(prefers-reduced-motion:reduce){{*{{transition:none!important}}}}
</style>
</head>
<body>
<script src="/js/nav.js" defer></script>

<main>
<section class="hero">
  <div class="tag-pill">{tl} &middot; {city_t}, {st} &middot; {month}</div>
  <h1>Are {city_t} {tl} Companies Invisible on Google?</h1>
  <p class="hero-sub">{hero_sub}</p>
  {f'<figure style="margin:0 0 40px;line-height:0;border-radius:16px;overflow:hidden"><img src="{trade_image}" alt="{tl} technician working in {city_t}, {st}" width="1200" height="440" loading="eager" fetchpriority="high" style="width:100%;height:380px;object-fit:cover;display:block;"></figure>' if trade_image else ''}
  <div class="stat-grid">
    <div class="stat-card">
      <div class="stat-num teal">{vol_display}</div>
      <div class="stat-label">people search for {tl} in {city_t} every month across these {total_kw} keyword phrases</div>
    </div>
    <div class="stat-card">
      <div class="stat-num danger">{lp_fired} of {total_kw}</div>
      <div class="stat-label">searches show a map pack of 3 local businesses — the most-clicked results on Google</div>
    </div>
    <div class="stat-card">
      <div class="stat-num">{top_appearances} of {total_kw}</div>
      <div class="stat-label">searches where {top_name_short} shows up in the {city_t} map — they're capturing your customers</div>
    </div>
    <div class="stat-card">
      <div class="stat-num teal">{rev_display}</div>
      <div class="stat-label">estimated monthly revenue for the {tl} company that owns the top spot on Google in {city_t}</div>
    </div>
  </div>
  <p class="data-note">Data pulled on {data_date} &middot; Simulates a {city_t}, {st} mobile search &middot; Results vary by searcher location, device, and date</p>
</section>

<hr class="section-divider">

<div class="stat-hook">
  <div class="stat-hook-grid">
    <div class="hook-stat">
      <div class="hook-num">97%</div>
      <div class="hook-label">of people research a local business online before calling</div>
    </div>
    <div class="hook-stat">
      <div class="hook-num">83%</div>
      <div class="hook-label">of those use Google — not Facebook, not Yelp, not Angi</div>
    </div>
    <div class="hook-stat">
      <div class="hook-num">92%</div>
      <div class="hook-label">pick a business from the first page — if you're not there, you don't exist</div>
    </div>
  </div>
</div>

<hr class="section-divider">

<section class="section">
  <div class="section-tag">Keywords Tracked</div>
  <h2>Every search we analyzed — and how many {city_t} customers type it every month</h2>
  <p class="section-sub">These are the exact phrases {city_t} residents type into Google when they need {tl}. Monthly volume is how many people searched that phrase in {city_t} last month.</p>
  <div class="table-scroll">
  <table class="kw-table" role="table">
    <thead>
      <tr>
        <th scope="col">Search phrase</th>
        <th scope="col">Monthly searches</th>
        <th scope="col">Map pack fires?</th>
      </tr>
    </thead>
    <tbody>
      {_build_kw_rows(keywords, volumes, stats)}
    </tbody>
  </table>
  </div>
  <p class="kw-total-row">Total: <strong>{vol_display} searches/month</strong> across all {total_kw} tracked keywords in {city_t}</p>
</section>

<hr class="section-divider">

<section class="section">
  <div class="section-tag">SERP Feature Analysis</div>
  <h2>What Google Shows for {tl} in {city_t}</h2>
  <p class="section-sub">Every search feature that appears — and how often — across all {total_kw} keywords we tracked.</p>
  <div class="table-scroll">
  <table class="feat-table" role="table">
    <thead>
      <tr>
        <th scope="col">Feature</th>
        <th scope="col">Fires on</th>
        <th scope="col">{mode_label}</th>
      </tr>
    </thead>
    <tbody>
      {feat_rows}
    </tbody>
  </table>
  </div>
</section>

<hr class="section-divider">

<section class="section">
  <div class="section-tag">Market Ownership</div>
  <h2>Who {city_t} Customers Find When They Search for {tl}</h2>
  <p class="section-sub">How many of the {total_kw} tracked searches each business appears in on the Google map pack — the most-clicked result on Google for local searches.</p>
  <div class="leader-card">
    <div>
      <div class="leader-badge">Current Market Leader</div>
      <div class="leader-name">{top_name}</div>
      <div class="leader-meta">
        {f'<div class="leader-meta-item"><span class="leader-stars">{stars_html}</span> <strong>{top_rating}</strong> out of 5</div>' if top_rating else ''}
        {f'<div class="leader-meta-item">💬 <strong>{top_reviews:,}</strong> Google reviews</div>' if top_reviews else ''}
        {f'<div class="leader-meta-item">📞 <strong>{top_phone}</strong></div>' if top_phone else ''}
        {f'<div class="leader-meta-item">🌐 <strong>{top_domain}</strong></div>' if top_domain and top_domain != "www.google.com" else ''}
      </div>
    </div>
    <div class="leader-stat">
      <div class="leader-stat-num">{top_appearances} of {total_kw}</div>
      <div class="leader-stat-label">searches where this<br>business appears<br>in the {city_t} map pack</div>
    </div>
  </div>
  {comp_bars}
</section>

<hr class="section-divider">

<section class="section">
  <div class="section-tag">Map Pack Position Breakdown</div>
  <h2>How Deeply Each Competitor Owns the {city_t} Map</h2>
  <p class="section-sub">Appearing in the map pack is one thing — but slot 1 gets significantly more clicks than slot 2 or 3. This shows where each competitor actually sits.</p>
  <div class="spread-insight">
    <strong>{top_name_short}</strong> holds slot&nbsp;1 on <strong>{leader_s1} of {total_kw}</strong> tracked searches — the single most-clicked position in the {city_t} {tl} market.
  </div>
  {spread_html}
</section>

<hr class="section-divider">

<section class="section">
  <div class="section-tag">Top Opportunity Keywords</div>
  <h2>Where a New Business Can Win in {city_t}</h2>
  <p class="section-sub">These are the {city_t} {tl} searches where the market leader does NOT have slot 1 locked — the highest-value keywords where the top map position is still up for grabs.</p>
  <div class="table-scroll">
  <table class="opp-table" role="table">
    <thead>
      <tr>
        <th scope="col">Search phrase</th>
        <th scope="col">Monthly searches</th>
        <th scope="col">Who's at slot 1 right now</th>
        <th scope="col">Is the market leader there?</th>
      </tr>
    </thead>
    <tbody>
      {opp_rows}
    </tbody>
  </table>
  </div>
  <p class="opp-note"><strong>Winnable</strong> = the market leader ({top_name_short}) is NOT at slot 1 for this keyword — a different competitor holds it, but that competitor is weaker and can be displaced. <strong>Leader owns it</strong> = {top_name_short} already holds slot 1 here.</p>
  {f'<p class="data-note" style="margin-top:8px">{open_count} of the top {len(opp_data)} high-volume keywords in {city_t} have an open slot 1 — no entrenched winner.</p>' if open_count else ''}
</section>

<hr class="section-divider">

<section class="section">
  <div class="section-tag">Visibility Gaps</div>
  <h2>What You're Missing</h2>
  <p class="section-sub">The features that fire most — and where your visibility is zero.</p>
  <div class="gap-grid">
    {gap_html}
  </div>
</section>

<hr class="section-divider">

{f'<div style="max-width:1000px;margin:0 auto;padding:0 40px 0"><figure style="line-height:0;border-radius:16px;overflow:hidden;margin-bottom:0"><img src="{trade_image}" alt="{tl} professionals serving {city_t}, {st}" width="1200" height="340" loading="lazy" style="width:100%;height:280px;object-fit:cover;display:block;"></figure></div>' if trade_image else ''}

<section class="rev-section">
  <div class="rev-banner">
    <div class="section-tag">Revenue Opportunity</div>
    <h2>How much money is sitting in {city_t} {tl} searches every month?</h2>
    <p>Here's what the math looks like for the business that owns the top spot on Google in {city_t}.</p>
    <div class="rev-steps">
      <div class="rev-step">
        <div class="rev-step-num">{vol_display}</div>
        <div class="rev-step-label">people search for {tl} in {city_t} every month</div>
        <div class="rev-step-formula">Total monthly search volume</div>
      </div>
      <div class="rev-step">
        <div class="rev-step-num">{rev['clicks']:,}</div>
        <div class="rev-step-label">of those clicks go to a business in the map pack</div>
        <div class="rev-step-formula">~12% click-through for a map pack listing</div>
      </div>
      <div class="rev-step">
        <div class="rev-step-num">{rev['leads']:,}</div>
        <div class="rev-step-label">of those visitors call or fill out a form</div>
        <div class="rev-step-formula">8% lead conversion — industry benchmark</div>
      </div>
      <div class="rev-step">
        <div class="rev-step-num">{rev['jobs']:,}</div>
        <div class="rev-step-label">of those leads turn into paying customers</div>
        <div class="rev-step-formula">40% close rate — typical for {tl}</div>
      </div>
      <div class="rev-step rev-total">
        <div class="rev-step-num">${rev['avg_ticket']:,}/job</div>
        <div class="rev-step-label">average {tl} job value in {city_t}</div>
        <div class="rev-step-formula">Industry average for this trade</div>
      </div>
      <div class="rev-step rev-total">
        <div class="rev-step-num">{rev_display}/mo</div>
        <div class="rev-step-label">estimated monthly revenue at the top of Google</div>
        <div class="rev-step-formula">Conservative estimate</div>
      </div>
    </div>
    <p class="rev-disclaimer">Estimates based on industry conversion benchmarks. Actual results vary by market, reviews, and site quality. The business currently in the top map-pack spot in {city_t} is: {top_name_short}.</p>
    <div class="ppc-callout">
      <div class="ppc-num">{ppc_display}/mo</div>
      <div class="ppc-label">That's what it would cost to buy these same clicks through Google Ads — at ~${rev['cpc']}/click for {tl} keywords in {city_t}. Ranking organically gets you those clicks for free, every month, without paying per click.</div>
    </div>
  </div>
</section>

<hr class="section-divider">

<section class="section">
  <div class="section-tag">Customer Questions</div>
  <h2>What {city_t} Customers Are Asking Google</h2>
  <p class="section-sub">These questions appeared in People Also Ask boxes across your tracked keywords. Each one is a content gap a competitor's site can own.</p>
  <ul class="paa-list">{paa_html}</ul>
</section>

<hr class="section-divider">

<div class="section">
  <div class="pitch">
    <h2>Here's what this means for your business.</h2>
    <p>Google has changed. Organic ranking alone used to be enough. Now, the first thing most customers see is the Local Pack — a map with three businesses, phone numbers, and star ratings. Below that are Local Services Ads with the Google Guaranteed badge. Your organic result, if you have one, comes after all of that.</p>
    <p>In the {city_t} {tl} market, the map pack fires on {lp_pct}% of searches. If you're not in it, you're invisible to most of the people searching for exactly what you do — before they ever scroll down to organic results.</p>
    <p>The businesses in that pack aren't necessarily better than you. They just have a stronger Google presence: an optimized Business Profile, consistent reviews, and a website that tells Google who they are and where they operate. That's fixable. Most businesses start showing up on Google Maps within 45–60 days of doing this work correctly.</p>
    <p>That's exactly what we do at CopperBuilds — <a href="/services.html">websites and local SEO built specifically for home service companies</a>. If you want to know what it would cost to fix your Google presence, <a href="/pricing.html">see our packages</a> or book a free call below.</p>
    <div class="internal-links">
      <a href="/services.html" class="internal-link">Our services for {tl} companies</a>
      <a href="/pricing.html" class="internal-link">See pricing</a>
      <a href="/blog/rank-google-maps.html" class="internal-link">How to rank on Google Maps</a>
    </div>
  </div>
</div>

<div class="cta-block">
  <h2>Ready to show up where {city_t} customers are searching?</h2>
  <p>We'll audit your current Google presence and show you exactly what to fix — for free.</p>
  <a href="/contact.html" class="btn-teal">Book a Free Strategy Call</a>
  <span class="cta-secondary">No commitment. No sales pitch. Just real data about your visibility.</span>
</div>
</main>

<footer style="background:var(--bg);border-top:1px solid var(--rule);padding:3.5rem 0 2rem" role="contentinfo">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a href="/index.html" aria-label="CopperBuilds homepage" style="display:inline-block;margin-bottom:1rem">
          <img src="/brand_assets/logo.svg" alt="CopperBuilds" height="36" style="display:block">
        </a>
        <p style="color:var(--warm-stone);font-size:.875rem;line-height:1.72;max-width:260px;margin-bottom:1.25rem">
          Websites and local SEO for home services pros across the USA. Built for small businesses. Not enterprise.
        </p>
        <div style="display:flex;gap:.625rem">
          <a href="https://www.facebook.com/CopperBuilds/" aria-label="CopperBuilds on Facebook" target="_blank" rel="noopener" style="display:flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:8px;border:1.5px solid var(--border);color:var(--warm-stone);text-decoration:none;transition:border-color .15s,background .15s,color .15s" onmouseover="this.style.borderColor='var(--accent-border)';this.style.background='var(--accent-dim)';this.style.color='var(--accent)'" onmouseout="this.style.borderColor='var(--border)';this.style.background='transparent';this.style.color='var(--warm-stone)'">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg>
          </a>
          <a href="https://www.linkedin.com/in/luisecharri/" aria-label="CopperBuilds on LinkedIn" target="_blank" rel="noopener" style="display:flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:8px;border:1.5px solid var(--border);color:var(--warm-stone);text-decoration:none;transition:border-color .15s,background .15s,color .15s" onmouseover="this.style.borderColor='var(--accent-border)';this.style.background='var(--accent-dim)';this.style.color='var(--accent)'" onmouseout="this.style.borderColor='var(--border)';this.style.background='transparent';this.style.color='var(--warm-stone)'">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="4"/><line x1="8" y1="11" x2="8" y2="16"/><circle cx="8" cy="8" r="1" fill="currentColor" stroke="none"/><path d="M12 11v5"/><path d="M12 11a3 3 0 016 0v5"/></svg>
          </a>
        </div>
      </div>
      <div>
        <h3 style="font-size:.8125rem;font-weight:700;color:var(--ink);margin-bottom:1rem;letter-spacing:.04em;text-transform:uppercase">Services</h3>
        <nav aria-label="Services footer links" style="display:flex;flex-direction:column;gap:.625rem">
          <a href="/services.html" style="color:var(--warm-stone);font-size:.875rem;text-decoration:none;transition:color .15s" onmouseover="this.style.color='var(--ink)'" onmouseout="this.style.color='var(--warm-stone)'">Web Design</a>
          <a href="/services.html" style="color:var(--warm-stone);font-size:.875rem;text-decoration:none;transition:color .15s" onmouseover="this.style.color='var(--ink)'" onmouseout="this.style.color='var(--warm-stone)'">Local SEO</a>
          <a href="/services.html" style="color:var(--warm-stone);font-size:.875rem;text-decoration:none;transition:color .15s" onmouseover="this.style.color='var(--ink)'" onmouseout="this.style.color='var(--warm-stone)'">Google Business</a>
          <a href="/pricing.html" style="color:var(--warm-stone);font-size:.875rem;text-decoration:none;transition:color .15s" onmouseover="this.style.color='var(--ink)'" onmouseout="this.style.color='var(--warm-stone)'">Pricing</a>
        </nav>
      </div>
      <div>
        <h3 style="font-size:.8125rem;font-weight:700;color:var(--ink);margin-bottom:1rem;letter-spacing:.04em;text-transform:uppercase">Company</h3>
        <nav aria-label="Company footer links" style="display:flex;flex-direction:column;gap:.625rem">
          <a href="/about.html"   style="color:var(--warm-stone);font-size:.875rem;text-decoration:none;transition:color .15s" onmouseover="this.style.color='var(--ink)'" onmouseout="this.style.color='var(--warm-stone)'">About</a>
          <a href="/blog.html"    style="color:var(--warm-stone);font-size:.875rem;text-decoration:none;transition:color .15s" onmouseover="this.style.color='var(--ink)'" onmouseout="this.style.color='var(--warm-stone)'">Blog</a>
          <a href="/reports/"     style="color:var(--warm-stone);font-size:.875rem;text-decoration:none;transition:color .15s" onmouseover="this.style.color='var(--ink)'" onmouseout="this.style.color='var(--warm-stone)'">Reports</a>
          <a href="/contact.html" style="color:var(--warm-stone);font-size:.875rem;text-decoration:none;transition:color .15s" onmouseover="this.style.color='var(--ink)'" onmouseout="this.style.color='var(--warm-stone)'">Contact</a>
        </nav>
      </div>
      <div>
        <h3 style="font-size:.8125rem;font-weight:700;color:var(--ink);margin-bottom:1rem;letter-spacing:.04em;text-transform:uppercase">Get Started</h3>
        <p style="color:var(--warm-stone);font-size:.875rem;line-height:1.65;margin-bottom:1rem">Ready to get your business found on Google?</p>
        <a href="/contact.html" class="btn btn-primary" style="font-size:.875rem;padding:.6875rem 1.25rem">Free Quote</a>
        <p style="color:var(--subtle);font-size:.8125rem;margin-top:.875rem">luis.copperbuilds@gmail.com</p>
      </div>
    </div>
    <hr class="rule">
    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;padding-top:1.5rem">
      <p style="color:var(--subtle);font-size:.8125rem">&copy; 2026 CopperBuilds. All rights reserved.</p>
      <p style="color:var(--subtle);font-size:.8125rem">Built for small businesses. Not enterprise.</p>
    </div>
  </div>
</footer>

</body>
</html>"""

# ── State Abbreviation → Full Name ───────────────────────────────────────────

STATE_NAMES = {
    "al":"Alabama","ak":"Alaska","az":"Arizona","ar":"Arkansas","ca":"California",
    "co":"Colorado","ct":"Connecticut","de":"Delaware","fl":"Florida","ga":"Georgia",
    "hi":"Hawaii","id":"Idaho","il":"Illinois","in":"Indiana","ia":"Iowa",
    "ks":"Kansas","ky":"Kentucky","la":"Louisiana","me":"Maine","md":"Maryland",
    "ma":"Massachusetts","mi":"Michigan","mn":"Minnesota","ms":"Mississippi",
    "mo":"Missouri","mt":"Montana","ne":"Nebraska","nv":"Nevada","nh":"New Hampshire",
    "nj":"New Jersey","nm":"New Mexico","ny":"New York","nc":"North Carolina",
    "nd":"North Dakota","oh":"Ohio","ok":"Oklahoma","or":"Oregon","pa":"Pennsylvania",
    "ri":"Rhode Island","sc":"South Carolina","sd":"South Dakota","tn":"Tennessee",
    "tx":"Texas","ut":"Utah","vt":"Vermont","va":"Virginia","wa":"Washington",
    "wv":"West Virginia","wi":"Wisconsin","wy":"Wyoming",
}

# ── CLI Main ──────────────────────────────────────────────────────────────────

def main():
    if not DFS_USER or not DFS_PASS:
        print("ERROR: DATAFORSEO_USERNAME / DATAFORSEO_PASSWORD missing in copperbuilds.env")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="CopperBuilds SERP Visibility Report Generator")
    parser.add_argument("--trade", required=True, choices=list(TRADE_SERP_KEYWORDS.keys()),
                        help="Trade vertical (e.g. hvac, plumbing, roofing)")
    parser.add_argument("--city", required=True, help="City name (e.g. phoenix)")
    parser.add_argument("--state", required=True, help="State abbreviation (e.g. az)")
    parser.add_argument("--domain", default=None, help="Client domain to track (optional)")
    parser.add_argument("--year", type=int, default=datetime.now().year, help="Report year")
    parser.add_argument("--dry-run", action="store_true",
                        help="Generate report with mock data (no API calls)")
    args = parser.parse_args()

    trade = args.trade.lower()
    city = args.city.lower().replace(" ", "-")
    state = args.state.lower()
    city_display = args.city.replace("-", " ")
    state_full = STATE_NAMES.get(state, args.state.upper())
    location = f"{city_display.title()},{state_full},United States"
    keywords = [f"{kw} {city_display.title()}" for kw in TRADE_SERP_KEYWORDS[trade]]

    slug = f"{trade.replace('_','-')}-seo-report-{city}-{state}-{args.year}"
    out_dir = Path(__file__).parent / "reports" / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        print(f"[DRY RUN] Using mock data for {len(keywords)} keywords")
        all_features = _mock_features(len(keywords), args.domain)
        volumes = {}
    else:
        all_features = []
        cache_hits = 0
        print(f"Pulling {len(keywords)} SERP results for {trade} in {city_display.title()}, {state.upper()}...")
        for i, kw in enumerate(keywords, 1):
            try:
                result, from_cache = dfs_serp_cached(kw, location)
                if from_cache:
                    cache_hits += 1
                    print(f"  [{i}/{len(keywords)}] {kw}  [cache]")
                else:
                    print(f"  [{i}/{len(keywords)}] {kw}  [live]")
                all_features.append(parse_features(result, args.domain))
            except Exception as e:
                print(f"  [{i}/{len(keywords)}] SKIP — {e}")
                all_features.append({})
        print(f"\n  {cache_hits}/{len(keywords)} keywords served from cache ({len(keywords)-cache_hits} live API calls)")

        # Fetch keyword search volumes — top-3 trades only (hvac, plumbing, roofing).
        # Other trades skip the volume call entirely to avoid unnecessary API spend.
        serp_kws = TRADE_SERP_KEYWORDS[trade]
        if trade in TRADE_VOLUME_KEYWORDS:
            vol_kws = list(TRADE_VOLUME_KEYWORDS[trade])
            print(f"Fetching search volumes for {len(vol_kws)} {trade} keywords...")
            try:
                raw_volumes = fetch_keyword_volumes(vol_kws, location, f"{trade}--{city}--{state}")
                # Map display keywords (with city) → volume using SERP subset for report table
                volumes = {keywords[i]: raw_volumes.get(serp_kws[i], 0)
                           for i in range(len(keywords))}
                total_vol = sum(volumes.values())
                print(f"  Total monthly searches (SERP keywords): {total_vol:,}")
                # Save full keyword map alongside the report — use for client onboarding.
                # Tiered by intent: 'service' keywords target money pages directly,
                # 'informational' keywords target blog/FAQ content only.
                kw_map = {k: {"volume": raw_volumes.get(k, 0), "tier": classify_keyword_intent(k)}
                          for k in vol_kws}
                service_vol = sum(v["volume"] for v in kw_map.values() if v["tier"] == "service")
                informational_vol = sum(v["volume"] for v in kw_map.values() if v["tier"] == "informational")
                service_count = sum(1 for v in kw_map.values() if v["tier"] == "service")
                informational_count = len(kw_map) - service_count
                kw_map_path = out_dir / "keyword-map.json"
                kw_map_path.write_text(
                    json.dumps({"trade": trade, "city": city_display, "state": state,
                                "location": location, "keyword_count": len(vol_kws),
                                "tier_summary": {
                                    "service": {"count": service_count, "monthly_searches": service_vol},
                                    "informational": {"count": informational_count,
                                                       "monthly_searches": informational_vol},
                                },
                                "keywords": kw_map}, ensure_ascii=False, indent=2),
                    encoding="utf-8",
                )
                print(f"  Keyword map saved: keyword-map.json ({len(vol_kws)} keywords)")
            except Exception as e:
                print(f"  Volume fetch failed: {e} — revenue section will show '—'")
                volumes = {}
        else:
            print(f"  Volume fetch skipped for {trade} (not a top-3 trade)")
            volumes = {}

    stats = aggregate_stats(all_features)
    competitors = aggregate_competitors(all_features)
    ownership = calc_ownership_score(all_features, args.domain)
    trade_img = TRADE_IMAGES.get(trade, "")
    html = generate_html(trade, city_display, args.state, args.year,
                         args.domain, keywords, stats, competitors, ownership, volumes, all_features,
                         trade_image=trade_img)

    out_path = out_dir / "index.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"\nReport saved: {out_path}")
    print(f"URL: copperbuilds.com/reports/{slug}/")

def _mock_features(n: int, domain: str | None) -> list:
    """Mock SERP feature data for dry-run / design preview."""
    import random
    random.seed(42)
    results = []
    competitors = ["Phoenix Pro HVAC", "Desert Air Systems", "SunState Cooling", "AZ Comfort Pros", "Valley HVAC Inc"]
    paa_q = [
        "How much does HVAC repair cost in Phoenix?",
        "What is the best HVAC company in Phoenix?",
        "How often should I service my AC in Arizona?",
        "Why is my AC not cooling my house in Phoenix?",
        "How long do HVAC systems last in the desert?",
        "What size AC unit do I need for a Phoenix home?",
        "Is it worth repairing an old AC unit?",
        "How do I find a licensed HVAC contractor in Arizona?",
    ]
    for _ in range(n):
        lp_fires = random.random() < 0.87
        lsa_fires = random.random() < 0.41
        ai_fires = random.random() < 0.34
        paa_fires = random.random() < 0.93
        fs_fires = random.random() < 0.22
        comp_pick = random.sample(competitors, min(3, len(competitors)))
        lp_businesses = [{"name": c, "url": f"https://{c.lower().replace(' ','-')}.com"} for c in comp_pick]
        results.append({
            "local_pack": {"fired": lp_fires, "businesses": lp_businesses if lp_fires else [],
                           "client_present": bool(domain) and random.random() < 0.1},
            "local_services": {"fired": lsa_fires, "businesses": [], "client_present": False},
            "organic": {"fired": True, "positions": [], "client_present": bool(domain) and random.random() < 0.2,
                        "client_rank": random.randint(4, 15) if domain else None},
            "featured_snippet": {"fired": fs_fires, "client_present": False},
            "ai_overview": {"fired": ai_fires, "client_present": False},
            "people_also_ask": {"fired": paa_fires, "questions": random.sample(paa_q, 3) if paa_fires else []},
            "images": {"fired": random.random() < 0.45},
        })
    return results

if __name__ == "__main__":
    main()
