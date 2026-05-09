# call sign: uv run run_day_2.py
from rich.console import Console

from app.chains import analyze_with_retry

console = Console()

sample_business_info = """
About Ideal
Ideal Real Estate
37 years, 5,200 happy families.
Established in 1982, the IDEAL Group has been building dream homes for thousands of happy families. Over the years, Ideal has gained the trust of its loyal customers by offering them high quality, comfortable homes as well as efficient commercial properties.

Headquartered in Kolkata, Ideal as a group has a pan India presence through its network of offices and business verticals. In the realty sector, having successfully completed several high-end real estate projects and with several more benchmark projects in the pipeline, the company has been transforming the skyline of Kolkata phenomenally.

Pillars of Trust
Thousands of satisfied customers and their trust in Ideal
As one of the leading players in the real estate market, Ideal endeavours to truly embody its tagline "Pillars of Trust" through its rich portfolio of world-class ready to move in, ongoing and upcoming real estate projects.

Going Green
More than 50 lakh sq. ft. of IGBC certified/ pre-certified Green Projects
Upholding the Group’s vision of creating value through sustainability, Ideal Real Estates Pvt. Ltd. takes pride in the Green buildings it continues to construct across various prominent and upcoming locales in Kolkata. Ideal has to its credit more than 50 lakh sq. ft. of IGBC certified/ pre-certified Green Projects. Catering to today’s environment conscious generation, Ideal’s green-certified properties are not only constructed using eco-friendly building materials and technology, but also offer features such as water harvesting infrastructure, solar panels and waste composting among others for continued sustainable living.

Other Group Businesses
Logistics Service - IDEAL Movers
Launched at the turn of the millennium with a modest fleet of 30 trailers, IDEAL Movers has emerged as one of the most preferred logistics partners of some of the largest companies in India. The Company today owns more than 1,850 mechanical trailers, hydraulic axles and more than 65 cranes ranging from 70T up to 600T capacity with recorded revenues of over 750 crores. Some of the Services offered by IDEAL Movers include –

Surface Logistics
Transportation of passenger cars using specialized car carriers
Specialized logistics solutions for project cargo
Yard management
Logistics solutions by rail
Logistics solutions for Indian ports
Equipment Rentals
The Group has also ventured into the heavy duty construction equipment rentals business. The Company provides various kinds of heavy duty cranes on rent to some of the largest manufacturing companies. It currently owns 65 cranes ranging from 80 MT to 600 MT and some of the companies under its list of prestigious clientele include –

Reliance Industries Ltd.
Wind World (Enercon India Ltd.)
Gamesa Wind Turbines Ltd
Larsen & Toubro Ltd
BPCL
Essar Projects (India) Ltd
BHEL
LANCO
Automotive Dealership
Ideal Group is a trusted dealer for Tata Motors and has been selling commercial vehicles in Bihar since 2000. The dealership’s state-of-the-art repairing facility in Muzaffarpur has made a mark as one of the largest motor workshops in Eastern India.

The showroom at Muzaffarpur offers all facilities under one roof – Sales, Service, Spares and Finance
Rated among Top 5 in the country by Tata Motors & No.1 in Eastern India
Muzaffarpur showroom houses 3 workshops and 50 bays
Network of 14 offices help cater to entire North Bihar
Turnover of 275 crores
Has successfully sold over 3000 vehicles in 2015/16
Alloys & Minerals Trading
The Ideal Group supplies raw materials of the highest quality at competitive rates to steel plants across India. Some of these alloys and minerals supplied include –

Raw Dolomite (40,000 ton/month)
High Carbon Ferro-Manganese (1,000 ton/month)
High Carbon Silico-Manganese (800 ton/month)
Low Carbon Silico-Manganese (500 ton/month)
Skulpt - Ideal Gymnasium
Skulpt is one of the largest gyms in Kolkata and operates through Ideal Gymnasium Pvt. Ltd. owned by the Ideal Group. Spread across an area of approximately 8000 sq. ft., Skulpt has an active member base of nearly 1200 members which is growing progressively. With state-of-the-art fitness equipment and amenities and a team of certified trainers and nutritionists, Skulpt has been able to carve a niche for itself in the fitness space.

Know more

Live the Dream
At Ideal, every project is a reflection of several dreams. A home that becomes an identity, an office address that is a city landmark, a property that defines a lifestyle statement. We give our best to help you find what you are looking for.
"""

# test case - 1
sample_business_info_test_1 = ""

# test case - 2
sample_business_info_test_2 = "Real estate company."

# test case - 3
sample_business_info_test_3 = "asdfghjkl qwerty 12345 !@#$%"

# test case - 4
sample_business_info_test_4 = (
    "A company operates in multiple domains and provides services globally."
)

# test case - 5
sample_business_info_test_5 = "A startup claims to be profitable but also reports heavy losses in recent quarters."


# input validation
def is_valid_input(text: str) -> bool:
    if len(text.strip()) > 10 and any(
        keyword in text.lower()
        for keyword in ["company", "business", "startup", "revenue"]
    ):
        return True
    return False


if __name__ == "__main__":
    console.rule("[bold red]AI Business Due Diligence Assistant - Day 2[/bold red]")
    console.rule("[bold blue]Business Due Diligence Analysis[/bold blue]")
    if not is_valid_input(sample_business_info):
        raise ValueError("Invalid input data for analysis")
    else:
        print(f"\nInput Text: {sample_business_info[:100]}...")
        result = analyze_with_retry(sample_business_info)  # type: ignore
        console.print(result)
