<?php
// db.php - MySQL 資料庫連線設定檔
// 使用前請修改以下四項資訊（從免費主機控制台取得）

$db_host   = 'localhost';          // ProFreeHost=localhost，InfinityFree=控制台顯示的主機位置
$db_name   = 'your_database_name'; // 資料庫名稱
$db_user   = 'your_database_user'; // 資料庫使用者
$db_pass   = 'your_database_pass'; // 資料庫密碼

// 建立連線
$conn = new mysqli($db_host, $db_user, $db_pass, $db_name);

// 檢查連線
if ($conn->connect_error) {
    die('資料庫連線失敗：' . $conn->connect_error);
}

// 設定字元編碼
$conn->set_charset('utf8mb4');

// 如需在其他頁面使用，引入本檔後即可用 $conn 變數
?>
