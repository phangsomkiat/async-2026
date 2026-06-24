from time import sleep, ctime, time

# ฟังก์ชันจำลองการอัปเดตหน้าจอ LCD ว่ากำลังจัดการคิวให้ลูกค้า
def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1) # จำลองการใช้เวลาอัปเดตระบบ 1 วินาที
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

# ฟังก์ชันจำลองการชงกาแฟ
def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1) # จำลองระยะเวลาชงกาแฟ 1 วินาที
    print(f"{ctime()} | Coffee ready for {customer_name}!")

def main():
    print(f"{ctime()} | === Synchronous Coffee Machine ===")
    start_time = time() # เริ่มจับเวลาการทำงานทั้งหมด
    
    # กำหนดคิวลูกค้า 3 คน
    queue = ['A', 'B', 'C']
    
    # วนลูปทำงานแบบ Synchronous (ต้องรอให้เสร็จทีละขั้นตอน ถึงจะไปขั้นต่อไปได้)
    for customer in queue:
        make_coffee(customer)       # ขั้นที่ 1: ชงกาแฟให้เสร็จก่อน
        update_cup_number(customer) # ขั้นที่ 2: อัปเดตสถานะหน้าจอตามหลัง
        
    # คำนวณเวลาที่ใช้ไปทั้งหมด
    total_time = time() - start_time
    print(f"{ctime()} | Total time: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()