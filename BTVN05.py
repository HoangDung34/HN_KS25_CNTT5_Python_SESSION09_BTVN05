order_list = [
    "GE001 - PENDING",
    "GE002 - ASSIGNED",
    "GE003 - DELIVERING"
]

while True:
    try:
            choice = int(input("""
            ===== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS =====
            1. Hiển thị danh sách đơn hàng
            2. Gán tài xế cho đơn hàng
            3. Cập nhật trạng thái giao hàng
            4. Hủy đơn hàng
            5. Thoát chương trình
        """))
    except:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    match choice:
        case 1:
            if len(order_list) == 0:
                print("Danh sách đơn hàng hiện đang trống")
            else:
                print("Danh sách đơn hàng hiện tại:")

                for index, order in enumerate(order_list, start=1):
                    print(f"{index}. {order}") 
        case 2:
            order_id = input("Nhập mã đơn hàng gán cho tài xế: ").strip().upper()
            find = False

            for index, order in enumerate(order_list):
                parts = order.split("-")
                id = parts[0]
                status = parts[1]

                if id == order_id:
                    find = True
                    
                    if status == "PENDING":
                        order_list[index] = f"{id} - ASSIGNED"

                        print(f"gán thành công tài xế: {order_list[index]}")
                    else:
                        print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý")

                    break
            
            if find == False:
                print("Không tìm thấy mã đơn hàng")
        case 3:
            order_id = input("Nhập mã đơn hàng cần cập nhật: ").strip().upper()
            find = False

            for index, order in enumerate(order_list):
                parts = order.split("-")
                id = parts[0]
                status = parts[1]

                if id == order_id:
                    find = True

                    if status == "ASSIGNED":
                        order_list[index] = f"{id} - DELIVERING"
                        print("Đơn hàng đang được giao")
                    elif status == "DELIVERING":
                        order_list[index] = f"{id} - COMPLETED"
                        print("Đơn hàng đã giao thành công")
                    elif status == "PENDING":
                        print("Đơn hàng chưa được gán tài xế, không thể chuyển sang trạng thái giao hàng")
                    elif status == "COMPLETED":
                        print("Đơn hàng đã hoàn tất, không thể cập nhật tiếp")
                    elif status == "CANCELLED":
                        print("Đơn hàng đã bị hủy, không thể cập nhật")
                    break
                if find == False:
                    print("Không tìm thấy mã đơn hàng")
        case 4:
            order_id = input("Nhập mã đơn hàng cần cập nhật: ").strip().upper()
            find = False

            for index, order in enumerate(order_list):
                parts = order.split("-")
                id = parts[0]
                status = parts[1]

                if id == order_id:
                    find = True

                    if status == "PENDING" or status == "ASSIGNED":
                        order_list[index] = f"{id} - CANCELLED"
                        print("Hủy đơn thành công")
                    elif status == "DELIVERING":
                        print("Đơn hàng đang được giao, không thể hủy")
                    elif status == "COMPLETED":
                        print("Đơn hàng đã hoàn tất, không thể hủy")
                    elif status == "CANCELLED":
                        print("Đơn hàng đã được hủy trước đó")
                    break    
                if find == False:
                    print("Không tìm thấy mã đơn hàng")
        case 5:
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ !!!")
