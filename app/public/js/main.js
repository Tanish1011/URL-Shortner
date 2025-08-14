document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("shorten-form");
    form?.addEventListener("submit", async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const payload = {
            url: formData.get("url"),
            alias: formData.get("alias") || null,
            expiresAt: formData.get("expiresAt") || null
        };
        const res = await fetch("/api/shorten", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(payload)
        });
        if (res.ok) {
            location.reload();
        } else {
            alert((await res.json()).detail);
        }
    });

    document.querySelectorAll(".copy-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            navigator.clipboard.writeText(btn.dataset.url);
            alert("Copied!");
        });
    });

    document.querySelectorAll(".delete-btn").forEach(btn => {
        btn.addEventListener("click", async () => {
            if (confirm("Delete this link?")) {
                const res = await fetch(`/api/${btn.dataset.code}`, {method: "DELETE"});
                if (res.ok) location.reload();
            }
        });
    });

    const toggle = document.getElementById("theme-toggle");
    if (toggle) {
        toggle.addEventListener("click", () => {
            document.documentElement.classList.toggle("dark");
            localStorage.setItem("theme", document.documentElement.classList.contains("dark") ? "dark" : "light");
        });
        if (localStorage.getItem("theme") === "dark") {
            document.documentElement.classList.add("dark");
        }
    }
});
