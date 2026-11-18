#!/usr/bin/env python3
"""Prepare platform research prompts and look up candidate entity matches."""

import sys
import json
from datetime import datetime, timezone
from urllib.parse import quote_plus

try:
    import requests
except ImportError:
    print("ERROR: Required packages not installed. Run: pip install -r requirements.txt")
    sys.exit(1)

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def check_youtube_presence(brand_name: str) -> dict:
    """Check brand presence on YouTube."""
    result = {
        "platform": "YouTube",
        "has_channel": None,
        "mentioned_in_videos": None,
        "search_url": f"https://www.youtube.com/results?search_query={quote_plus(brand_name)}",
        "recommendations": [],
    }

    # Note: Actual YouTube API would be used in production
    # Record an observation only after reviewing the search results.
    result["check_instructions"] = [
        f"Search YouTube for '{brand_name}' and check:",
        "1. Does the brand have an official YouTube channel?",
        "2. Are there videos FROM the brand (tutorials, demos, thought leadership)?",
        "3. Are there videos ABOUT the brand from other creators?",
        "4. What's the view count on brand-related videos?",
        "5. Are there positive reviews or demonstrations?",
    ]

    result["recommendations"] = [
        "Create a YouTube channel if none exists",
        "Publish educational/tutorial content related to your niche",
        "Encourage customers to create review/demo videos",
        "Optimize video titles and descriptions with brand name",
        "Add timestamps and chapters to improve AI parseability",
        "Include transcripts (YouTube auto-generates, but review for accuracy)",
    ]

    return result


def check_reddit_presence(brand_name: str) -> dict:
    """Check brand presence on Reddit."""
    result = {
        "platform": "Reddit",
        "has_subreddit": None,
        "mentioned_in_discussions": None,
        "search_url": f"https://www.reddit.com/search/?q={quote_plus(brand_name)}",
        "recommendations": [],
    }

    result["check_instructions"] = [
        f"Search Reddit for '{brand_name}' and check:",
        "1. Does the brand have its own subreddit (r/brandname)?",
        "2. Is the brand discussed in relevant industry subreddits?",
        "3. What's the sentiment (positive, negative, neutral)?",
        "4. Are there recommendation threads mentioning the brand?",
        "5. Does the brand have an official Reddit presence?",
        "6. Are mentions recent (within last 6 months)?",
    ]

    result["recommendations"] = [
        "Monitor relevant subreddits for brand mentions",
        "Participate authentically in industry discussions (no spam)",
        "Create an official Reddit account for customer support",
        "Share valuable content (not just self-promotion)",
        "Respond to questions about your product/service category",
        "Reddit authenticity matters — don't use marketing speak",
    ]

    return result


def check_wikipedia_presence(brand_name: str) -> dict:
    """Check brand/entity presence on Wikipedia and Wikidata."""
    result = {
        "platform": "Wikipedia",
        "has_wikipedia_page": None,
        "has_wikidata_entry": None,
        "cited_in_articles": None,
        "search_url": f"https://en.wikipedia.org/wiki/Special:Search?search={quote_plus(brand_name)}",
        "wikidata_url": f"https://www.wikidata.org/w/index.php?search={quote_plus(brand_name)}",
        "recommendations": [],
    }

    # Check Wikipedia API
    try:
        api_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={quote_plus(brand_name)}&format=json"
        response = requests.get(api_url, headers=DEFAULT_HEADERS, timeout=15)
        if response.status_code == 200:
            data = response.json()
            search_results = data.get("query", {}).get("search", [])
            if search_results:
                # Check if top result is about the brand
                top_title = search_results[0].get("title", "").lower()
                if brand_name.lower() in top_title:
                    result["candidate_wikipedia_title"] = search_results[0]["title"]
                result["wikipedia_search_results"] = len(search_results)
    except Exception:
        pass

    # Check Wikidata
    try:
        wikidata_url = f"https://www.wikidata.org/w/api.php?action=wbsearchentities&search={quote_plus(brand_name)}&language=en&format=json"
        response = requests.get(wikidata_url, headers=DEFAULT_HEADERS, timeout=15)
        if response.status_code == 200:
            data = response.json()
            entities = data.get("search", [])
            if entities:
                result["wikidata_id"] = entities[0].get("id", "")
                result["wikidata_description"] = entities[0].get("description", "")
    except Exception:
        pass

    result["recommendations"] = [
        "If eligible, create a Wikipedia article (requires notability criteria)",
        "Ensure Wikidata entry exists with complete structured data",
        "Add sameAs links in schema markup pointing to Wikipedia/Wikidata",
        "Get cited in existing Wikipedia articles as a source",
        "Build notability through press coverage and independent reviews",
        "Note: Wikipedia has strict notability guidelines — PR coverage helps establish this",
    ]

    return result


def check_linkedin_presence(brand_name: str) -> dict:
    """Check brand presence on LinkedIn."""
    result = {
        "platform": "LinkedIn",
        "has_company_page": None,
        "employee_thought_leadership": None,
        "search_url": f"https://www.linkedin.com/search/results/companies/?keywords={quote_plus(brand_name)}",
        "recommendations": [],
    }

    result["check_instructions"] = [
        f"Search LinkedIn for '{brand_name}' and check:",
        "1. Does the company have a LinkedIn page?",
        "2. How many followers?",
        "3. Is the page active with recent posts?",
        "4. Do employees post thought leadership content?",
        "5. Are there LinkedIn articles about the brand?",
        "6. Is there engagement on posts (likes, comments, shares)?",
    ]

    result["recommendations"] = [
        "Create/optimize LinkedIn company page",
        "Post regular thought leadership content",
        "Encourage employees to share company content",
        "Publish long-form LinkedIn articles",
        "Engage with industry discussions and comments",
        "Add company LinkedIn URL to schema sameAs property",
    ]

    return result


def check_other_platforms(brand_name: str) -> dict:
    """Check brand presence on additional platforms."""
    result = {
        "platform": "Other Platforms",
        "platforms_checked": {},
        "recommendations": [],
    }

    platforms = {
        "Quora": f"https://www.quora.com/search?q={quote_plus(brand_name)}",
        "Stack Overflow": f"https://stackoverflow.com/search?q={quote_plus(brand_name)}",
        "GitHub": f"https://github.com/search?q={quote_plus(brand_name)}",
        "Crunchbase": f"https://www.crunchbase.com/textsearch?q={quote_plus(brand_name)}",
        "Product Hunt": f"https://www.producthunt.com/search?q={quote_plus(brand_name)}",
        "G2": f"https://www.g2.com/search?utf8=&query={quote_plus(brand_name)}",
        "Trustpilot": f"https://www.trustpilot.com/search?query={quote_plus(brand_name)}",
    }

    result["platforms_checked"] = {
        name: {
            "search_url": url,
            "check_instruction": f"Search for '{brand_name}' on {name}",
        }
        for name, url in platforms.items()
    }

    result["recommendations"] = [
        "Maintain profiles on industry-relevant platforms",
        "Respond to questions on Quora and Stack Overflow",
        "Encourage customer reviews on G2 and Trustpilot",
        "Keep Crunchbase profile updated (important for B2B)",
        "Open-source contributions on GitHub boost developer brand authority",
        "Product Hunt launch can generate significant initial buzz",
    ]

    return result


def generate_brand_report(brand_name: str, domain: str = None) -> dict:
    """Generate a comprehensive brand mention report."""
    report = {
        "brand_name": brand_name,
        "domain": domain,
        "analysis_date": datetime.now(timezone.utc).date().isoformat(),
        "scope": "Search prompts and candidate entity matches. Verify identity with cited URLs.",
        "platforms": {},
        "overall_recommendations": [],
    }

    # Check all platforms
    report["platforms"]["youtube"] = check_youtube_presence(brand_name)
    report["platforms"]["reddit"] = check_reddit_presence(brand_name)
    report["platforms"]["wikipedia"] = check_wikipedia_presence(brand_name)
    report["platforms"]["linkedin"] = check_linkedin_presence(brand_name)
    report["platforms"]["other"] = check_other_platforms(brand_name)

    return report


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python brand_scanner.py <brand_name> [domain]")
        print("Example: python brand_scanner.py 'Acme Corp' acmecorp.com")
        sys.exit(1)

    brand = sys.argv[1]
    domain = sys.argv[2] if len(sys.argv) > 2 else None

    result = generate_brand_report(brand, domain)
    print(json.dumps(result, indent=2, default=str))
