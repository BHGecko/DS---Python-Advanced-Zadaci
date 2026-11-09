import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("weather_tokyo_data.csv")

df["full_date"] = pd.to_datetime(
    df["year"].astype(str) + "/" + df["day"], format="%Y/%m/%d"
)

df["temperature"] = df["temperature"].astype(str).str.replace(
    r"[^\d.-]", "", regex=True
)

df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
df = df.dropna(subset=["temperature", "full_date"])

df = df.sort_values(by="full_date").reset_index(drop=True)

print("Podaci uspješno učitani i pripremljeni.\n")


avg_temp = df["temperature"].mean()
print("--- ZADATAK 1: PROSJEČNA TEMPERATURA ---")
print(f"Prosječna temperatura svih dana: {avg_temp:.2f} °C\n")


df["month"] = df["full_date"].dt.month
monthly_avg = df.groupby("month")["temperature"].mean()

print("--- ZADATAK 2: PROSJEČNA TEMPERATURA PO MJESECIMA ---")
print(monthly_avg.round(2))
print()

plt.figure(figsize=(9, 5))
plt.bar(monthly_avg.index, monthly_avg.values, color="skyblue", edgecolor="black")
plt.title("Prosječna mjesečna temperatura u Tokiju", fontsize=13)
plt.xlabel("Mjesec", fontsize=11)
plt.ylabel("Prosječna temperatura (°C)", fontsize=11)
plt.xticks(range(1, 13))
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()


hottest_row = df.loc[df["temperature"].idxmax()]
coldest_row = df.loc[df["temperature"].idxmin()]

print("--- ZADATAK 3: NAJTOPLIJI I NAJHLADNIJI DAN ---")
print("Najtopliji dan:")
print(hottest_row.to_string())
print("\nNajhladniji dan:")
print(coldest_row.to_string())
print()


plt.figure(figsize=(12, 5))
plt.plot(
    df["full_date"],
    df["temperature"],
    color="crimson",
    linewidth=1.2,
    label="Temperatura (°C)",
)
plt.title("Promjene temperature kroz vrijeme (Tokio)", fontsize=13)
plt.xlabel("Datum", fontsize=11)
plt.ylabel("Temperatura (°C)", fontsize=11)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()


def map_season(month):
  if month in [12, 1, 2]:
    return "Zima"
  elif month in [3, 4, 5]:
    return "Proljeće"
  elif month in [6, 7, 8]:
    return "Ljeto"
  elif month in [9, 10, 11]:
    return "Jesen"


df["season"] = df["month"].apply(map_season)

season_order = ["Zima", "Proljeće", "Ljeto", "Jesen"]
seasonal_avg = (
    df.groupby("season")["temperature"].mean().reindex(season_order)
)

print("--- ZADATAK 5: PROSJEČNA TEMPERATURA PO GODIŠNJIM DOBIMA ---")
print(seasonal_avg.round(2))
print()

plt.figure(figsize=(8, 4.5))
plt.plot(
    seasonal_avg.index,
    seasonal_avg.values,
    marker="o",
    color="darkorange",
    linewidth=2,
    markersize=7,
)
plt.title("Prosječna temperatura po godišnjim dobima", fontsize=13)
plt.xlabel("Godišnje doba", fontsize=11)
plt.ylabel("Prosječna temperatura (°C)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()