import { GoogleSpreadsheet } from "google-spreadsheet";
import env from "dotenv";
env.config();
import { createRequire } from "module";
const require = createRequire(import.meta.url);
const secrets = require("../google_secrets.json");

(async () => {
  const doc = new GoogleSpreadsheet(process.env.GOOGLE_SHEET_ID);

  await doc.useServiceAccountAuth({
    client_email: secrets.client_email,
    private_key: secrets.private_key,
  });

  await doc.loadInfo();

  const personSheet = doc.sheetsByTitle["people"];
  const rows = await personSheet.getRows();
  console.log(rows[0].name);
  rows[2].age = 50;
  rows[2].save();

  rows[0].delete();
})();
