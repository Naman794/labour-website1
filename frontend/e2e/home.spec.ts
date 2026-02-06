import { test, expect } from "@playwright/test";

test("homepage loads", async ({ page }) => {
  await page.goto("/");
  await expect(
    page.getByRole("heading", { name: /find work fast/i }),
  ).toBeVisible();
});

test("random route shows 404", async ({ page }) => {
  await page.goto("/random");
  await expect(page.getByRole("heading", { name: /page not found/i })).toBeVisible();
});
