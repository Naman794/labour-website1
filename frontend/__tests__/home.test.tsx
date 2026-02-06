import { render, screen } from "@testing-library/react";
import HomePage from "../app/page";

describe("HomePage", () => {
  it("renders the headline", () => {
    render(<HomePage />);
    expect(
      screen.getByRole("heading", {
        name: /find work fast\. hire workers faster\./i,
      }),
    ).toBeInTheDocument();
  });

  it("renders the primary call-to-action buttons", () => {
    render(<HomePage />);
    expect(screen.getByRole("button", { name: /find jobs/i })).toBeInTheDocument();
    expect(
      screen.getByRole("button", { name: /hire workers/i }),
    ).toBeInTheDocument();
  });
});
