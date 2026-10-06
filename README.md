# Hệ thống quản lý nhân viên

Đây là dự án ứng dụng console được xây dựng bằng C# và .NET,
tập trung vào việc thực hành lập trình hướng đối tượng (OOP),
CRUD, kiểm tra dữ liệu đầu vào và lưu trữ dữ liệu bằng JSON.

## 1. Chức năng

- Thêm nhân viên
- Xem danh sách nhân viên
- Tìm kiếm nhân viên theo tên
- Cập nhật thông tin nhân viên
- Xóa nhân viên
- Kiểm tra dữ liệu đầu vào
- Lưu và đọc dữ liệu bằng JSON
- Thống kê nhân viên
- Tính lương trung bình
- Tìm nhân viên có mức lương cao nhất
- Thống kê số lượng nhân viên theo phòng ban

## 2. Công nghệ sử dụng

- C#
- .NET 10
- System.Text.Json
- Console Application

## 3. Cấu trúc dự án

```text
csharp-management-system/
├── Models/
│   └── Employee.cs
│
├── Services/
│   ├── EmployeeService.cs
│   └── InputHelper.cs
│
├── Program.cs
├── employees.json
└── README.md