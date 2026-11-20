from prometheus_client import start_http_server, Summary, Gauge
import random
import time

total_deliveries = Gauge("total_deliveries", "Total number of deliveries")
pending_deliveries = Gauge("pending_deliveries", "Number of pending deliveries")
on_the_way_deliveries = Gauge("on_the_way_deliveries", "Number of deliveries on the way")
average_delivery_time = Summary("average_delivery_time", "Average delivery time in seconds")

def simulate_delivery():
    pending = random.randint(10, 20)
    on_the_way = random.randint(5, 20)
    delivered = random.randint(30, 70)
    avg_time = random.uniform(15, 45)

    total = pending + on_the_way + delivered

    total_deliveries.set(total)
    pending_deliveries.set(pending)
    on_the_way_deliveries.set(on_the_way)
    average_delivery_time.observe(avg_time)

    return {
        "total": total,
        "pending": pending,
        "on_the_way": on_the_way,
        "delivered": delivered,
        "avg_time": avg_time
    }

if __name__ == "__main__":
    print("[INFO] Starting delivery metrics exporter on port 8000...", flush=True)
    start_http_server(8000, addr="0.0.0.0")
    while True:
        data = simulate_delivery()
        print(f"[DEBUG] Total={data['total']}, Pending={data['pending']}, AvgTime={data['avg_time']:.2f}s", flush=True)
        time.sleep(2)