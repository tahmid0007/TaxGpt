import os
from typing import List
from bsup import download_html
import html2text
from requests_html import HTMLSession


def download_and_save_in_markdown(url: str, dir_path: str) -> None:
    """Download the HTML content from the web page and save it as a markdown file."""
    # Extract a filename from the URL
    if url.endswith("/"):
        url = url[:-1]

    filename = url.split("/")[-1] + ".md"
    print(f"Downloading {url} into {filename}...")

    session = HTMLSession()
    response = session.get(url, timeout=30)

    # Render the page, which will execute JavaScript
    response.html.render()

    # Convert the rendered HTML content to markdown
    h = html2text.HTML2Text()
    markdown_content = h.handle(response.html.raw_html.decode("utf-8"))

    # Write the markdown content to a file
    filename = os.path.join(dir_path, filename)
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(markdown_content)


def download(pages: List[str]) -> str:
    """Download the HTML content from the pages and save them as markdown files."""
    # Create the content/notion directory if it doesn't exist
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(base_dir, "content", "blogs")
    os.makedirs(dir_path, exist_ok=True)
    for page in pages:
        download_and_save_in_markdown(page, dir_path)
    return 


PAGES = [
    "https://hallandwilcox.com.au/thinking/a-guide-to-taxation-in-australia/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/what-is-capital-gains-tax/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/list-of-cgt-assets-and-exemptions/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/acquiring-cgt-assets/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/cgt-events/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/cgt-discount/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/calculating-your-cgt/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/eligibility-for-main-residence-exemption/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/moving-to-a-new-main-residence/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/treating-former-home-as-main-residence/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/living-separately-to-your-spouse-or-children/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/using-your-home-for-rental-or-business/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/building-or-renovating-your-home/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/destruction-of-your-home/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/compulsory-acquisition-of-your-home/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/property-and-capital-gains-tax/your-main-residence-home/home-on-more-than-2-hectares/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/shares-and-similar-investments/when-cgt-applies-to-shares-and-units/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/shares-and-similar-investments/keeping-records-of-shares-and-units/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/shares-and-similar-investments/share-investing-versus-share-trading/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/shares-and-similar-investments/when-you-can-claim-losses-on-shares-and-units/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/shares-and-similar-investments/share-buy-backs/",
    "https://www.ato.gov.au/forms-and-instructions/capital-gains-tax-guide-2023/part-a-about-capital-gains-tax/how-to-work-out-your-capital-gain-or-capital-loss?anchor=How_to_work_out_your_capital_gain_or_cap#How_to_work_out_your_capital_gain_or_cap/",
    "https://www.ato.gov.au/forms-and-instructions/capital-gains-tax-guide-2023/part-a-about-capital-gains-tax/real-estate-and-main-residence?anchor=Real_estate_and_main_residence#Real_estate_and_main_residence/",
    "https://www.ato.gov.au/forms-and-instructions/capital-gains-tax-guide-2023/part-a-about-capital-gains-tax/investments-in-shares-and-units?anchor=Investments_in_shares_and_units#Investments_in_shares_and_units",
    "https://www.ato.gov.au/forms-and-instructions/capital-gains-tax-guide-2023/part-a-about-capital-gains-tax/does-capital-gains-tax-apply-to-you?anchor=Does_capital_gains_tax_apply_to_you#Does_capital_gains_tax_apply_to_you/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/residential-rental-properties/rental-income-you-must-declare/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/residential-rental-properties/rental-expenses-to-claim/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/residential-rental-properties/rental-expenses-to-claim/",
    "https://www.ato.gov.au/individuals-and-families/investments-and-assets/residential-rental-properties/top-10-tips-to-help-rental-property-owners/",
    "https://www.taxwarehouse.com.au/australian-tax-basics-explained/",
    "https://www.superguide.com.au/how-super-works/income-tax-rates-brackets/",
    "https://insiderguides.com.au/tax-guide-for-international-students/"
    ]

if __name__ == "__main__":
    download(PAGES)
