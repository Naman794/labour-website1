import { access } from "node:fs/promises";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = join(__dirname, "..");
const playwrightPath = join(rootDir, "node_modules", "@playwright", "test");

async function main() {
  try {
    await access(playwrightPath);
  } catch {
    console.log("Playwright not installed, skipping e2e");
    process.exit(0);
  }

  const command = join(rootDir, "node_modules", ".bin", "playwright");
  const child = spawn(command, ["test"], {
    stdio: "inherit",
    cwd: rootDir,
    shell: true,
  });

  child.on("exit", (code) => {
    process.exit(code ?? 0);
  });
}

main();
