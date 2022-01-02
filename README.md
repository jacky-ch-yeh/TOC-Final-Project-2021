# TOC Project 2021
> Linebot 實作
> Due date: 2022/1/2 12pm

## 創立主旨
身為電資學院的一份子，一定都對將來就業有很多憧憬，  
但我們每天忙碌於課業，對於台灣的科技公司(特別是本土)卻十分不了解，  
於是我就想做出一個能讓我們更能了解、關心科技業的app，  
並讓我們能力更提升，視野更廣闊

## 介紹
### 基本資訊
名稱：TechBot  
![](https://cdn.discordapp.com/attachments/755734650613399613/927122751095963688/unknown.png)  

首先先幫我加入一下好友 :3
可以使用搜尋ID(記得要打"@")或掃QR Code  

![image](https://user-images.githubusercontent.com/76469551/147871487-066199af-766c-4c2a-a228-5eb10f83946a.png)  

### 功能  
這是它的選單，接下來介紹他的功能哦  
![image](https://user-images.githubusercontent.com/76469551/147871361-4694f246-59a3-4cee-9fff-7ea684ef097d.png)  

1. 找話題: 它可以尋找有趣的話題(支援重新找一個話題)
2. 探索公司: 它可以選擇不同類型的科技廠，並介紹選擇的企業
3. 科技業職稱簡介: 它可以介紹各種職位的簡稱
4. 精進自己: 它可以推薦實用的Coding/Reading網站，讓我們學習並進步  


+ 沒有進過職場的我們一定都很好奇業界的前輩在關心什麼，或是別人拿到什麼offer和他如何選擇  
  這時就可以透過「找話題」，TechBot會推薦一個話題文章給你，同時不喜歡也可以換一篇文章  
![](https://cdn.discordapp.com/attachments/755734650613399613/927129041004277760/unknown.png)  

+ 透過「探索公司」，可以根據選擇的公司類型，找到感興趣的企業，  
  然後去更了解這間公司的背景，並透過股價了解它大致的發展  
![](https://cdn.discordapp.com/attachments/755734650613399613/927129085585551390/unknown.png)  
+ 以IC廠為例  
![image](https://user-images.githubusercontent.com/76469551/147871713-96842979-fdc1-4ae9-a862-9047214e12a8.png)  
+ 以聯發科為例  
![](https://cdn.discordapp.com/attachments/755734650613399613/927129155483619378/unknown.png)  

+ 我們常常看人家在討論職場生活時，都會講到一些簡稱，  
  像是RD、PM和PIE等等，每次都搞不清楚這些是什麼意思
  
  這時就可以使用「科技業職稱簡介」，它會介紹各種常見的職位簡稱，  
  這樣就不會每次都聽不懂很多前輩在說什麼職稱了  
![](https://cdn.discordapp.com/attachments/755734650613399613/927129200262021150/unknown.png)  

+ 在閒暇之餘，我們也要不忘提升自己，  
  這時選擇「精進自己」，他會根據你想提升的面向(Coding/Reading)，來提供對應的網站  
![](https://cdn.discordapp.com/attachments/755734650613399613/927129241827557446/unknown.png)  
+ 以閱讀為例
![](https://cdn.discordapp.com/attachments/755734650613399613/927129281585360896/unknown.png)  

## Fsm 結構圖  
![](https://cdn.discordapp.com/attachments/755734650613399613/927122068535902238/fsm.png)  
### state說明
- user: 輸入主選單/menu開始使用TechBot
- menu: 選擇要使用的功能(按紐)
- article: 顯示出推薦的文章，並選擇要退回主選單還是重新推薦
- info: 選擇感興趣的科技廠類別
- ic: 選擇感興趣的ic廠
- system: 選擇感興趣的系統廠
- show_info: 顯示選擇的企業簡介，並選擇要回到主選單或是去看看其他類別的廠
- position: 顯示職稱的縮寫介紹
- website: 選擇要提升閱讀方面還是coding
- coding: 顯示出有關coding的網站
- reading: 顯示出報導科技的相關網站

## 環境
- ubuntu 18.04
- python 3.6.9

## 技術
- Beautifulsoup4
    - 爬取企業的股價
    - 爬取企業在維基百科上的簡介


> 作者：　葉承軒／成功大學資訊系112
> 最後編輯時間：　2022/1/2

