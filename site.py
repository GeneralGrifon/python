#! /user/bin/env python3

print("Content-type: text/html")
print()

html1 = """ 
<html> 
    <head> 
        <script> 
             function f1() { 
                 return "hello"; 
             } 
        </script> 
        <style> 
            div { 
                
                height: 333px;
                background: url("https://cdn.shopify.com/s/files/1/0469/5814/9798/files/formento5_1944x.jpg?v=1616757769");
                transition: 1s;
                justify-content: center;
                text-align: center;
                
                
            }
            div:hover { 
                
                background: url("https://a-static.besthdwallpaper.com/put-v-wild-green-forest-oboi-1920x1080-26869_48.jpg");
                
                height: 777px;
            }
            a
            {
            font-size: 50px;
            color: #FFF;
            cursour; pointer;
            text-decoration: none;
            position: relative;
            top: 50%;
            transition: 2s;
            }
            div:hover a
            {
            font-size: 90px;
            color: black;
            }
            
        </style> 
    </head> 
    <body> 
        <div id='title'> 
            <a href='https://color.adobe.com/ru/create/color-wheel' onclick='f1();'>COCK MY SUCK</a> 
        </div> 
    </body> 
</html>""" 
print (html1) 
