import { chromium } from "@playwright/test";
import * as fs from "fs";
import { Parser } from "json2csv";

/**
 * 練習問題
 * 3ページ目の役職が係長の人物名と会社名をすべてtest-data.csvに出力しなさい。
 * ※会社名が取れない場合にも処理が止まらないように例外処理を追加してください。
 *
 * "company","name"
 * "山本金属株式会社","28 伊藤 友美"
 */
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto("http://localhost:3000");

  const page3Locator = page.locator(".page-link.page-number >> nth=2");
  await page3Locator.click();

  const cardLocators = page.locator(".cards.list-group-item");
  const cardCount = await cardLocators.count();

  const fetchedCards = [];
  for (let i = 0; i < cardCount; i++) {
    const cardLocator = cardLocators.locator(`nth=${i} >> a`);
    const cardText = await cardLocator.textContent();

    await cardLocator.click();

    let companyText = "";
    try {
      const companyLocator = page.locator(".card-title.company");
      companyText = await companyLocator.textContent();
    } catch (e) {}

    const divisionLocator = page.locator(".division");
    const divisionText = await divisionLocator.textContent();
    if (!divisionText.includes("係長")) {
      const backLocator = page.locator("text=戻る");
      await backLocator.click();
      continue;
    }

    fetchedCards.push({
      company: companyText,
      name: cardText,
      division: divisionText,
    });

    const backLocator = page.locator("text=戻る");
    await backLocator.click();
  }

  await browser.close();

  const parser = new Parser();
  const csv = parser.parse(fetchedCards);

  fs.writeFileSync("./text-data.csv", csv);
})();