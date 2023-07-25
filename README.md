*(Hướng dẫn gốc của [r/placevn](https://discord.gg/r-placevietnam-960076480916901948) và r/osuplace, cảm ơn mọi người)*
-------
<h1 align="center">
  <img src="./img/MIXIFINAL-quangminhnd.png" alt="r/place vietnam">

  <a href="https://discord.gg/r-placevietnam-960076480916901948">Tham gia Discord MixiGaming và theo dõi trên các nguồn khác để tác chiến, mong các bạn không đánh đơn lẻ</a>
</h1>


# SAU ĐÂY SẼ LÀ HƯỚNG DẪN ĐỂ CÁC BẠN CÓ THỂ SỬ DỤNG ĐƯỢC CÁC CÔNG CỤ VẼ ARTWORK !

## TAMPERMONKEY


*Tampermonkey là công cụ để bạn có thể manipulate những gì bạn thấy trên trang web của mình.*

### Cài đặt: 

- Nếu bạn xài Chrome: https://chrome.google.com/webstore/detail/dhdgffkkebhmkfjojejmpbldmpobfkfo
- Nếu bạn xài Edge: https://microsoftedge.microsoft.com/addons/detail/iikmkjmpaadaobahmlepeloendndfphd
- Nếu bạn xài Firefox: https://addons.mozilla.org/en-US/firefox/addon/tampermonkey/
- Nếu bạn xài Safari: https://apps.apple.com/us/app/tampermonkey/id1482490089
- Nếu bạn xài Opera: https://addons.opera.com/en/extensions/details/tampermonkey-beta/

Chỉ cần nhấn vào Install Extension, bạn đã cài đặt được Tampermonkey cho trình duyệt của bạn. Đây là extension cần có để chạy tiếp 2 công cụ ở phía dưới đây. 
## KHUNG OVERLAY

*Khung overlay (hay template/ template - manager) là công cụ để các bạn có thể nhìn thấy những ô màu mà chúng mình cập nhật, từ đó các bạn sẽ biết vẽ ô nào là màu nào.*
- Cài đặt: https://github.com/osuplace/templateManager/raw/main/dist/templateManager.user.js
![Tampermonkey](img/tampermk.png)

- Click vào link bên trên -> Nhấn Install khi tab mới hiện ra
Image
- Vào trang chủ của sự kiện r/place (reddit.com/r/place), sẽ thấy nút settings màu trắng trôi lơ lững như bên dưới. Click vào đó sẽ hiện ra menu như hình dưới.
Image
Tại ô "Template URL", paste đường link bên dưới vào và bấm "Always Load". Sau khi F5 lại trang, bạn sẽ thấy những chấm cần tô hiện đè (overlay) trên màn hình r/place

Link: https://raw.githubusercontent.com/LiquidRekto/rplacevnhideout/master/vnflag.json
Image


Đây là file JSON (chính thức?) của r/placevietnam.

Hãy kiểm tra update của script overlay!
-----------------
- Làm lại bước 2 :)

Hướng dẫn setup:
-----------------

1. Tải [Tampermonkey](https://www.tampermonkey.net/)

![tampermonkey](https://i.imgur.com/WPz6Kcg.png)

2. Tải [script overlay](https://github.com/osuplace/templateManager/raw/main/dist/templateManager.user.js)

![overlay](https://i.imgur.com/uKwMWei.png)

3.1. [Vào template](https://new.reddit.com/r/place/?jsontemplate=https://raw.githubusercontent.com/LiquidRekto/rplacevnhideout/master/vnflag.json)

Lưu ý: nếu không thấy template thì hãy reload

3.2. Nếu cách này không được thì vào menu cài đặt 
![options](https://i.imgur.com/MK4J8sq.png) 
và dán link **https://raw.githubusercontent.com/LiquidRekto/rplacevnhideout/master/vnflag.json** vào mục "Template URL"

4. Nhấn "Always allow all domains"
![menu](https://media.discordapp.net/attachments/1131430894511607870/1131655632987111617/image.png)

<h3>Video hướng dẫn setup</h3>

https://github.com/ntbeastboy/rplacevietnam/assets/99698334/0d6baaae-b78a-4e8e-a8b3-4d77904ffb51

Hướng dẫn setup bot treo máy
---------------------------------------
Bạn không muốn dành cả ngày ngồi trên máy tính đặt pixel? Muốn cống hiến cho r/place trong lúc bạn ngủ? Hãy tải autoscript ngay!
Nếu bạn đã tải tampermonkey thì hãy nhấn link phía dưới, nếu không, hãy xem phần trên
Reload để script có tác dụng
<h2> 

[Tải ngay script treo máy](https://github.com/j4pa0/placevn/raw/main/placevn-userscript.user.js)

</h2>

Một vài tính năng của phần mềm overlay
----------------------------------------
Sau khi nhấn vào nút options ![options](https://i.imgur.com/MK4J8sq.png) , một menu sẽ hiện ra

![menu](https://i.imgur.com/sgFaRAQ.png)

Có 2 tính năng:
1. Preview template in full: Xem trước template
2. Dither amount: Để ở mức 1/3:

![dither](https://media.discordapp.net/attachments/1131429795721388112/1131862836373639199/image.png)

FAQ
-------------------
1. Tình trạng overlay không trùng với khối.

![menu](https://media.discordapp.net/attachments/1131429845683937450/1131899383089217616/image.png?width=860&height=678)

**Fix**: Chỉnh "Scale & layout" trong windows setting xuống 100%

![menu](https://media.discordapp.net/attachments/1131429845683937450/1131899948749836298/image.png?width=1286&height=682)

Design mới
--------------------

Có design mới? 
1. Upload ảnh design của bạn trên [imgur](https://imgur.com/) (nhớ up đúng dimension của lãnh thổ cập nhật trên discord)
2. Gửi link ảnh vào #place-art

Update tọa độ
-------------------
Tọa độ tính theo kiểu khác nên vào https://charity.pxls.space/ để place design rồi thay coordinate vào file JSON


