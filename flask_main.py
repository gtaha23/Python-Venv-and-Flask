from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
    "Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
    "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
    "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
    "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
    "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
    "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
    "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."
]

@app.route("/")
def hello_world():
    return '<h1>Merhaba! rastgele gerçeklikler görmek ister misin? <a href="/rastgele_gerceklikler">Bana tıkla!</a></h1>'

@app.route("/rastgele_gerceklikler")
def rastgele_gerceklikler():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/scp_birlikleri")
def scp_birlik():
    return f'Demek gizli sayfayı buldun! işte sana bazı S.C.P mtf birlikleri: / 1.Alpha-1 - 2.Tau-5 - 3.Beta-7 - 4.Omega-12 - 5.Omega-7 - 6.Epsilon-11 - 7.GRU-P - 8.Nu-7 - 9.Zeta-9 - 10.Alpha-4 - 11.Alpha-9 - 12.Gamma-5 - 13.Gamma-6 - 14.Gamma-13 - 15.Delta-5 - 16.Epsilon-9 - 17.Eta-10 - 18.Eta-11 - 19.Theta-4 - 20.Theta-90 - 21.Iota-10 - 22.Kappa-10 - 23.Lambda-5 - 24.Lambda-12 - 25.Lambda-14 - 26.Mu-3 - 27.Mu-4 - 28.Mu-13 - 29.Epsilon-6 - 30.Pı-1 - 31.Sigma-66 - 32.Psi-7 - 33.Psi-8 - 34.Omega-0 \ Güncellemeler son hızıyla devam ediyor 📢.'

@app.route("/scp")
def scp():
    return f'Bu sayfada ise sana bazı S.C.P anomalilerini söyleyeceğim: / S.C.P-096, S.C.P-173, S.C.P-1000, S.C.P-724, S.C.P-536, S.C.P-348,S.C.P-999, S.C.P-1474, S.C.P-895, S.C.P-786, S.C.P-234, S.C.P-123, S.C.P-859, S.C.P-111, S.C.P-564, S.C.P-195 \ Güncellemeler Son hızıyla devam ediyor 📢.'

app.run(debug=True)
