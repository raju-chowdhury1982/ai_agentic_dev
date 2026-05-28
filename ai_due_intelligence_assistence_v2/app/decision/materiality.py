MATERIAL_MISSING_TERMS: list[str] = [
    "financial data",
    "financial performance",
    "cash flow",
    "profitability",
    "market analysis",
    "legal dispute",
    "regulatory",
    "debt",
]

NON_MATERIAL_MISSING_TERMS: list[str] = [
    "future growth plans",
    "investment requirements",
    "technology roadmap",
    "competitor analysis details",
    "market share data",
]


def has_material_missing_info(missing_items: list[str]) -> bool:
    """Find the missing terms in given input data"""
    lowered_items = [item.lower() for item in missing_items]

    return any(
        term in item for item in lowered_items for term in MATERIAL_MISSING_TERMS
    )
