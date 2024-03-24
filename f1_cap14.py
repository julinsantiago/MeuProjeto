{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red174\green176\blue183;\red23\green23\blue26;\red117\green114\blue185;
\red89\green158\blue96;\red195\green123\blue90;\red38\green157\blue169;}
{\*\expandedcolortbl;;\csgenericrgb\c68235\c69020\c71765;\csgenericrgb\c9020\c9020\c10196;\csgenericrgb\c45882\c44706\c72549;
\csgenericrgb\c34902\c61961\c37647;\csgenericrgb\c76471\c48235\c35294;\csgenericrgb\c14902\c61569\c66275;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 CALCULADORA\
\
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f1\fs26 \cf2 \cb3 valor1 = \cf4 input\cf2 (\cf5 "Por favor, digite o primeiro valor: "\cf2 )\
valor2 = \cf4 input \cf2 (\cf5 "Por favor, digite o segundo valor: "\cf2 )\
soma = \cf4 float\cf2 (valor1) + \cf4 float\cf2 (valor2)\
\cf4 print\cf2 (\cf5 f"A soma entre os valores \'e9 \cf6 \{\cf2 soma\cf6 \}\cf5 "\cf2 )\
subtracao = \cf4 float\cf2 (valor1) - \cf4 float\cf2 (valor2)\
\cf4 print\cf2 (\cf5 f"A subtra\'e7\'e3o dos valores \'e9 \cf6 \{\cf2 subtracao\cf6 \}\cf5 "\cf2 )\
multiplicacao = \cf4 float\cf2 (valor1) * \cf4 int\cf2 (valor2)\
\cf4 print\cf2 (\cf5 f"A multiplica\'e7\'e3o dos valores \'e9 \cf6 \{\cf2 multiplicacao\cf6 \}\cf5 "\cf2 )\
divisao = \cf4 float\cf2 (valor1) / \cf4 float\cf2 (valor2)\
\cf4 print\cf2 (\cf5 f"A divis\'e3o dos valores \'e9 \cf6 \{\cf2 divisao\cf6 \}\cf5 "\cf2 )\
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf2 \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf4 print\cf2 (\cf5 "esse programa calcula a velocidade m\'e9dia de um patinete"\cf2 )\
distancia = \cf4 input\cf2 (\cf5 "Qual foi a dist\'e2ncia em metros percorrida pelo patinete: "\cf2 )\
tempo = \cf4 input\cf2 (\cf5 "Quantos minutos o patinete demorou para percorrer essa distancia?: "\cf2 )\
velocidade_media = \cf4 float\cf2 (distancia) / \cf4 float\cf2 (tempo)\
\cf4 print\cf2 (\cf5 f"A velocidade m\'e9dia do patinete foi de \cf6 \{\cf2 velocidade_media\cf6 \}\cf5 m/min"\cf2 )\
\
\
\cf4 print \cf2 (\cf5 "esse programa inverte os conte\'fados de duas vari\'e1veis"\cf2 )\
A = \cf4 input\cf2 (\cf5 "Digite o conteudo da variavel A: "\cf2 )\
B = \cf4 input\cf2 (\cf5 "Digite o conte\'fado da vari\'e1vel B: "\cf2 )\
troca = A\
A = B\
B = troca\
\cf4 print \cf2 (\cf5 f"Agora que trocamos, a vari\'e1vel A cont\'e9m \cf6 \{\cf2 A\cf6 \}\cf5  e a vari\'e1vel B contem \cf6 \{\cf2 B\cf6 \}\cf5 "\cf2 )\
\
cliente_vip = \cf4 input\cf2 (\cf5 "Informe se o cliente \'e9 VIP: "\cf2 )\
peso_bagagem = \cf4 input\cf2 (\cf5 "Informe o peso da bagagem: "\cf2 )\
\cf6 if \cf2 cliente_vip == \cf5 "sim"\cf2 :\
    \cf6 if \cf4 float\cf2 (peso_bagagem) > \cf7 \cb3 32\cf2 \cb3 :\
        \cf4 print\cf2 (\cf5 "Sua bagagem est\'e1 acima do permitido."\cf2 )\
    \cf6 else\cf2 :\
        \cf4 print\cf2 (\cf5 "Cliente VIP com peso de bagagem permitido"\cf2 )\
\cf6 else\cf2 :\
    \cf6 if \cf4 float\cf2 (peso_bagagem) > \cf7 \cb3 23\cf2 \cb3 :\
        \cf4 print\cf2 (\cf5 "Sua bagagem est\'e1 acima do peso permitido."\cf2 )\
    \cf6 else\cf2 :\
        \cf4 print\cf2 (\cf5 "Sua bagagem est\'e1 com o peso permitido."\cf2 )\
\
parente = \cf4 input\cf2 (\cf5 "Digite a rela\'e7\'e3o familiar do Julio: "\cf2 )\
\cf6 if \cf2 parente == \cf5 "mae"\cf2 :\
    \cf4 print\cf2 (\cf5 "lidia maria"\cf2 )\
\cf6 elif \cf2 parente == \cf5 "pai"\cf2 :\
    \cf4 print\cf2 (\cf5 "euler santiago"\cf2 )\
\cf6 elif \cf2 parente == \cf5 "irma"\cf2 :\
    \cf4 print\cf2 (\cf5 "ana luiza"\cf2 )\
\cf6 elif \cf2 parente == \cf5 "sobrinha velha"\cf2 :\
    \cf4 print\cf2 (\cf5 "luluzinha"\cf2 )\
\cf6 elif \cf2 parente == \cf5 "sobrinha meio"\cf2 :\
    \cf4 print\cf2 (\cf5 "lalazinha"\cf2 )\
\cf6 elif \cf2 parente == \cf5 "sobrinha nova"\cf2 :\
    \cf4 print\cf2 (\cf5 "bibizinha"\cf2 )\
\cf6 else\cf2 :\
    \cf4 print\cf2 (\cf5 "algum tio, tia ou primo"\cf2 )\
\
valor_compra = \cf4 float\cf2 (\cf4 input\cf2 (\cf5 "Digite o valor da compra: "\cf2 ))\
cupom_desconto = \cf4 input\cf2 (\cf5 "Digite o nome do cupom de desconto: "\cf2 )\
valor_final = \cf4 float\cf2 (valor_compra)*\cf7 \cb3 0.9\
\
\cf6 \cb3 if \cf2 cupom_desconto == \cf5 "niver10"\cf2 :\
    \cf4 print \cf2 (\cf5 f"O valor final da compra \'e9 \cf6 \{\cf2 valor_final\cf6 \}\cf5 "\cf2 )\
\cf6 else\cf2 :\
    \cf4 print\cf2 (\cf5 f"Cupom inv\'e1lido. O valor final da compra \'e9 \cf6 \{\cf2 valor_compra\cf6 \}\cf5 "\cf2 )\
\
\
}