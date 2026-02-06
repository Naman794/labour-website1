export default function HomePage() {
  return (
    <main className="flex min-h-screen items-center justify-center px-6">
      <section className="max-w-2xl text-center">
        <p className="text-sm uppercase tracking-[0.2em] text-slate-400">
          Labour Marketplace
        </p>
        <h1 className="mt-4 text-4xl font-semibold text-white md:text-5xl">
          Find Work Fast. Hire Workers Faster.
        </h1>
        <div className="mt-8 flex flex-col items-center justify-center gap-4 sm:flex-row">
          <button className="rounded-full bg-white px-6 py-3 text-sm font-semibold text-slate-900 transition hover:bg-slate-100">
            Find Jobs
          </button>
          <button className="rounded-full border border-white/40 px-6 py-3 text-sm font-semibold text-white transition hover:border-white">
            Hire Workers
          </button>
        </div>
      </section>
    </main>
  );
}
