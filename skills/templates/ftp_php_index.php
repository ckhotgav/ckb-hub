<?php
// 引入資料庫連線
require_once 'db.php';

// === 訪客計數器 ===

// 先查詢目前計數
$result = $conn->query("SELECT count FROM visitor_count WHERE id = 1");
if ($result && $result->num_rows > 0) {
    $row = $result->fetch_assoc();
    $count = $row['count'] + 1;
} else {
    $count = 1;
}

// 更新計數（使用 REPLACE 或 UPDATE + INSERT）
$stmt = $conn->prepare("REPLACE INTO visitor_count (id, count) VALUES (1, ?)");
$stmt->bind_param("i", $count);
$stmt->execute();
$stmt->close();
?>
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>訪客計數器 - 點哥AI全能工具箱</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', system-ui, sans-serif; background: #0d1117; color: #c9d1d9; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
        .container { text-align: center; background: #161b22; border: 1px solid #30363d; border-radius: 16px; padding: 3rem 4rem; max-width: 500px; }
        h1 { font-size: 2rem; margin-bottom: 1rem; background: linear-gradient(90deg, #58a6ff, #3fb950); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .count { font-size: 4rem; font-weight: bold; color: #f0883e; margin: 1rem 0; }
        .status { color: #3fb950; margin-bottom: 1rem; }
        .footer { color: #8b949e; font-size: 0.85rem; margin-top: 2rem; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 訪客計數器</h1>
        <div class="status">✅ 資料庫連線成功</div>
        <div class="count"><?php echo $count; ?></div>
        <p>你是第 <strong><?php echo $count; ?></strong> 位訪客！</p>
        <div class="footer">PHP + MySQL 動態網站示範</div>
    </div>
</body>
</html>
