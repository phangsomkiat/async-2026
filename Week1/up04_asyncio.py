from time import ctime, time, process_time
import asyncio
import os
import threading
import psutil

# ฟังก์ชันอัปเดตหน้าจอ LCD (แบบ Async)
async def update_cup_number(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    task_id = id(asyncio.current_task())

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Task: {task_id}] LCD: Processing for customer {customer_name}...")
    sum(i * i for i in range(1000000)) # จำลองการประมวลผล CPU
    await asyncio.sleep(1) # หน่วงเวลา 1 วินาที (แบบไม่บล็อกระบบ)
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Task: {task_id}] LCD: Done for customer {customer_name}.")

# ฟังก์ชันชงกาแฟ (แบบ Async)
async def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    task_id = id(asyncio.current_task())

    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Task: {task_id}] Making coffee for {customer_name}...")
    sum(i * i for i in range(1000000)) # จำลองการประมวลผล CPU
    await asyncio.sleep(1) # หน่วงเวลา 1 วินาที (แบบไม่บล็อกระบบ)
    print(f"{ctime()} | [PID: {pid}] [TID: {thread_id}] [Task: {task_id}] Coffee ready for {customer_name}!")

# ฟังก์ชันตัวกลางเพื่อรวมขั้นตอนชงกาแฟและอัปเดตจอเข้าด้วยกันให้ลูกค้า 1 คน
async def serve_customer(customer_name):
    await make_coffee(customer_name)
    await update_cup_number(customer_name)

async def main():
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id
    print(f"{ctime()} | [Main PID: {main_pid}] [Main TID: {main_tid}] === Asyncio Coffee Machine ===")

    start_time = time()
    start_cpu = process_time()

    queue = ['A', 'B', 'C']
    tasks = []

    # วนลูปสร้าง Task ให้ลูกค้าทุกคน (สั่งให้เริ่มทำงานพร้อมกันแบบสลับคิว)
    for customer in queue:
        # โยนฟังก์ชัน serve_customer เข้าไปเป็น Task ของระบบ Asyncio
        task = asyncio.create_task(serve_customer(customer), name=f"Task-{customer}")
        tasks.append(task)

    # รอจนกว่าทุก Task (ลูกค้าทุกคน) จะได้รับบริการจนเสร็จครบถ้วน
    await asyncio.gather(*tasks)

    # สรุปผลลัพธ์การใช้ทรัพยากร
    duration = time() - start_time
    cpu_duration = process_time() - start_cpu

    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)

    print(f"\n[Summary Asyncio]")
    print(f"Total Wall Time: {duration:0.2f} seconds")
    print(f"Total CPU Time: {cpu_duration:0.4f} seconds")
    print(f"Total Memory (RAM): {mem_mb:.2f} MB")

if __name__ == "__main__":
    asyncio.run(main())