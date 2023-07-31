import numpy as np
def sum_n (n):
	tong = 0
	while(n != 0):
		tong += n%10
		n = int(n/10)
	return tong
print("Enter your day")
day = int(input())
print("Enter your month")
month = int(input())
print("Enter your year")
year = int(input())
life_number = sum_n(day) + sum_n(month) + sum_n(year)
if (life_number > 11):
	life_number = sum_n(life_number)
d = {2:"Trong thần học thì con số 2 chính là một con số khá đặc biệt và hiếm có. Do đó, số lượng người có con số  chủ đạo là số 2 là tương đối ít. Với những người có con số này thường là người rất nhạy cảm với mọi vấn đề xảy ra. Họ cũng là người luôn sẵn sàng giúp đỡ những người khác.Những con  người sở hữu số 2 đặc biệt họ khó có thể  trở thành lãnh đạo. Nhưng lại làm việc cực tốt khi được dưới trướng của một vị lãnh đạo vô cùng năng động. Người mang số 2 không có tham vọng lớn luôn làm việc độc lập và tìm kiếm  những lối đi riêng cho mình. Họ luôn trung thành và tận tụy trong mọi công việc mà họ làm.Bên cạnh đó, thì người mang số 2 lại không có khả năng làm việc dưới áp lực công việc cường độ cao. Họ chỉ thích một tốc độ làm việc vừa phải dưới sự phối  hợp nhịp nhàng. Cùng với đó, những người mang số 2 thường dựa dẫm nhiều vào lý trí mà bỏ qua trực giác. Chính điều này sẽ khiến cho những người có con số chủ đạo là số 2 thường mắc phải một số phán đoán sai lầm nhất định."
     ,3:"Con số chủ đạo 3 là một con số mạnh ở phần tư duy và lý luận. Với những người am hiểu về Nhân số học thì đều biết số 3 được tính ở đầu bảng của trục ngang Trí não. Với những người mang con số này mục đích chính đều liên quan tới khả năng tư duy và suy nghĩ của mình. Người số 3 là  người luôn thể hiện sự tỉnh táo, sắc sảo trong mỗi công việc mà họ làm. Những người mang số 3 luôn là người không chỉ có đầu óc nhanh nhạy mà còn có óc hài hước. Họ luôn rất lý trí trong mọi việc không hề làm việc theo cảm tính. Tuy nhiên, tính cách của họ thường dễ thương với những người mới quen. Nhưng với những người đã gắn bó lâu dài họ rất hay bắt lỗi. Vì vậy, người người thân thiết với họ luôn cảm thấy  khó chịu bởi tính cách này. Là nam giới có con số chủ đạo là số 3 họ thường thể hiện sự gia trưởng và thích chỉ đạo người khác. Cùng với đó họ thường lý trí nên khó bao dung với những người không được  may mắn hơn họ về trí não.Một số công việc phù hợp với những con người mang số chủ đạo là số 4 đó là lĩnh vực khoa học, nghiên cứu, phần mềm, phân tích hệ thống, quản trị kinh doanh. Hoặc cũng có thể theo đuổi các nhà lý luận phê bình hay các vai diễn trong showbiz"
     ,4:"Trong trường hợp con số chủ đạo là số 4 chúng có hai trường hợp đó là số 4 bình thường và số 4 đặc biệt được tạo ra từ con số 22. Xét về chỉ số đường đời thì những người mang con số này họ chỉ chú trọng đến giá trị vật chất. Họ chỉ thích nói chuyện và làm những việc mà đem lại lợi ích về giá trị của họ.Với con người số 4 khi còn trẻ thường chú trọng và quan tâm đến vật chất. Nhưng khi về già thì họ lại quan tâm và chú trọng đến trí tuệ, sức khỏe và tinh thần. Người số 4 là những người có năng lực tổ chức và rất đáng tin cậy."
     ,5:"Với những người mang con số chủ đạo 5 là người không thích sự ràng buộc nào cả. Họ luôn yêu thích sự tự do. Đây là những con người có cảm xúc rất sâu sắc và một trực giác tốt, họ chính là điển hình của những người sống nội tâm phong phú.Người mang số 5 luôn sở hữu một tư duy sâu sắc họ  mang trong mình tính nghệ thuật, luôn hóm hỉnh và tràn đầy nhiệt huyết trong suy nghĩ và lối sống. Người số 5 chính là người thích đi theo đám đông họ không làm theo bất cứ một nguyên tắc hay truyền thống nào cả.Bên cạnh đó, họ cũng là một mẫu người rất giàu lòng trắc ẩn luôn giúp đỡ và chia sẻ với mọi người để họ có được một cuộc sống tích cực hơn nữa.  Những con người mang số 5 thường có những suy nghĩ tích cực luôn tò mò và hiếu kỳ với mọi thứ xung quanh. Chính sự yêu thích tự do nên những con người này thường phù hợp với startup hoặc làm Freelancer"
     ,6:"Người mang con số 6 thần số học là những người với khả năng sáng tạo luôn có trách nhiệm với bản thân và công việc họ làm. Những con người này thường yêu thương mọi người ghét sự bất công. Họ luôn bao bọc che chở những con người xung quanh mình. Tuy nhiên, những con người này đôi khi lại vị gán trách nhiệm vô cớ và bị lợi dụng. Vì vậy họ cần phải biết tự bảo vệ bản thân mình.Với người số 6 họ là người luôn vì gia đình luôn muốn xây dựng và bảo vệ tổ ấm của mình một cách tốt nhất. Vì vậy là người số 6 họ luôn có trách nhiệm với gia đình là người đáng tin nhất. Những con người này luôn thích sự bình yên mà không muốn sự tranh cãi hay đấu tranh vì vậy họ có xu hướng cam chịu. Đây chính là nhược điểm của con người mang số 6 chủ đạo."
     ,7:"Con số chủ đạo 7 trong thần số học là những người rất năng động trong cuộc sống. Họ luôn khát khao có thể tự trải nghiệm mọi điều trong cuộc sống. Họ không dễ dàng tin bất cứ điều gì hay làm theo bất cứ ai. Số 7 là những con người rất tin vào bản thân không than vãn.Những người mang số 7 thường thích học hỏi theo tính cách của mình. Họ luôn mong muốn trở thành người đi chia sẻ hơn là những người lắng nghe. Ngoài ra, những con người này họ không chịu học hỏi những kinh nghiệm của người khác chính vì vậy họ thường gặp nhiều những thất bại không đáng có."
     ,8:"Con số chủ đạo 8 thần số học là những người có tính cách rất mạnh mẽ, họ luôn sống độc lập và là chỗ dựa đáng tin cậy nhất. Những con người này ít thể hiện cảm xúc hay tình cảm. Chính điều này mà nhiều người nhận xét họ là những người lạnh lùng, thờ ơ và vô cùng lạnh nhạt. Những con người này thường khó mở lời trong việc yêu thương và lòng biết ơn đối với người khác.  Dẫu vậy, bên trong con người họ vẫn có lòng trắc ẩn  cảm  thông vô hạn với những người có hoàn cảnh không được may mắn như mình.Người số 8 là người có thể kiểm soát cảm xúc rất tốt nên không để cảm xúc ảnh hưởng đến quyết định của mình. Chính vì vậy, các công việc phù hợp với họ là những công việc liên quan đến quản lý. Chắc chắn họ sẽ hoàn thành tốt được nhiệm vụ của mình."
     ,9:"Những con người mang con số chủ đạo số 9 là mẫu người của xã hội. Họ luôn là mẫu người phục vụ lợi ích cho toàn xã hội và luôn đặt yếu tố của con người lên hàng đầu. Những con người này luôn hướng về nghệ thuật và nhân văn hơn là các công việc về kinh doanh, thương mại.Con số 9 chủ đạo là người rất trách nhiệm, trung thực và đáng tin cậy nhất. Họ luôn mong muốn được phục vụ và nâng cao đời sống của con người. Tuy nhiên, những con người mang số 9 chủ đạo họ lại có nhược điểm đó chính là thiếu đi sự kiên nhẫn, kiên định. Họ dễ bị bỏ dở giữa chừng mà không đi đến cuối cùng để có thể kết thúc được chúng.Những con người này làm việc theo cảm hứng rất mạn. Nghĩa là khi họ có cảm hứng thì mới làm còn không thì họ sẵn sàng bỏ dở giữa chừng. Những người này họ không giỏi trong việc nhìn người dễ bị người khác lợi dụng."
     ,10:"Những con người mang số chủ đạo là số 10 thường là những người rất dễ thích nghi và linh hoạt trong mọi hoàn cảnh. Họ còn là những con người luôn vui vẻ, hòa đồng luôn được nhiều người yêu thích và tiếp nhận. Những con người này thường rất thẳng thắn, tự tin và vô cùng hòa nhã.Với những con người này họ luôn có máu nghệ sĩ trong người và rất có thể trở thành một nghệ sĩ tài ba vẹn toàn. Người số 10 chủ đạo không giỏi trong việc giải quyết các vấn đề tâm lý của bản thân hay của những người khác. Chính vì vậy họ rất dễ tiêu cực và nhiều khi trở nên lạc lối."
     ,11:"Con số chủ đạo 11 trong thần số học là con số cuối cùng thể hiện một con người có khả năng phát triển về tâm linh vô cùng mạnh mẽ. Họ luôn là những con người đầy trách nhiệm. Tuy nhiên, rất nhiều người có con số này không nhận ra được năng lực của mình. Họ luôn bị vật chất của cuộc sống cám dỗ."}
print("Your life number is : ",life_number)
print("Y nghia : ",d[life_number])
year_now = int(input("Enter the moment year : "))
person_number = sum_n(day) + sum_n(month) + sum_n(year_now)
if(person_number > 9):
	person_number = sum_n(person_number)
print("your person number is : ", person_number)
d2 = {1:"NĂM CỦA SỰ ĐIỀU CHỈNH QUYẾT LIỆT"
      ,2:"NĂM CỦA SỰ PHÁT TRIỂN TÂM LINH VÀ CHIA SẺ"
      ,3:"NĂM CỦA SỰ MỞ MANG TÂM TRÍ"
      ,4:"NĂM CỦA SỰ CỦNG CỐ NỘI LỰC"
      ,5:"NĂM CỦA TỰ DO"
      ,6:"NĂM CỦA SỰ SÁNG TẠO"
      ,7:"NĂM CỦA SỰ TẬP TRUNG VƯỢT CHƯỚNG NGẠI"
      ,8:"NĂM CỦA SỰ ĐỘC LẬP VÀ TRÍ TUỆ"
      ,9:"NĂM ĐỈNH ĐIỂM THAY ĐỔI"}
print("y nghia : ",d2[person_number])
if ((month == 3 and day >=21) or (month ==4 and day <=19)):
	print("Your constellation is  : Aries(Ram)")
elif ((month == 4 and day >=20) or (month ==5 and day <=20)):
	print("Your constellation is  : Taurus(Bull)")
elif ((month == 5 and day >=21) or (month ==6 and day <=21)):
	print("Your constellation is  : Gemini (Twins)")
elif ((month == 6 and day >=22) or (month ==7 and day <=22)):
	print("Your constellation is  : Cancer (Crab)")
elif ((month == 7 and day >=23) or (month ==8 and day <=22)):
	print("Your constellation is  : Leo (Lion)")
elif ((month == 8 and day >=23) or (month ==9 and day <=22)):
	print("Your constellation is  : Virgo (Virgin)")
elif ((month == 9 and day >=23) or (month ==10 and day <=23)):
	print("Your constellation is  : Libra (Balance)")
elif ((month == 10 and day >=24) or (month ==11 and day <=21)):
	print("Your constellation is  : Scorpius (Scorpion)")
elif ((month == 11 and day >=22) or (month ==12 and day <=21)):
	print("Your constellation is  : Sagittarius (Archer)")
elif ((month == 12 and day >=22) or (month ==11 and day <=19)):
	print("Your constellation is  : Capricornus (Goat)")
elif ((month == 1 and day >=20) or (month ==2 and day <=18)):
	print("Your constellation is  : Aquarius (Water Bearer)")
elif ((month == 2 and day >=19) or (month ==3 and day <=20)):
	print("Your constellation is  : Pisces (Fish)")
#c
print("Ho va Ten :")
ten_old=input()
ten=ten_old.upper()
destiny=0;
for i in np.arange(0,len(ten)):
    if(ten[i] == 'A' or ten[i] == 'J' or ten[i] == 'S'):
        value=1
    elif(ten[i] == 'B' or ten[i] == 'K' or ten[i] == 'T'):
        value=2
    elif(ten[i] == 'C' or ten[i] == 'L' or ten[i] == 'U'):
        value=3
    elif(ten[i] == 'D' or ten[i] == 'M' or ten[i] == 'V'):
        value=4
    elif(ten[i] == 'E' or ten[i] == 'N' or ten[i] == 'W'):
        value=5
    elif(ten[i] == 'F' or ten[i] == 'O' or ten[i] == 'X'):
        value=6   
    elif(ten[i] == 'G' or ten[i] == 'P' or ten[i] == 'Y'):
        value=7
    elif(ten[i] == 'H' or ten[i] == 'Q' or ten[i] == 'Z'):
        value=8
    elif(ten[i] == 'I' or ten[i] == 'R'):
        value=9
    else:
        value=0
    destiny=destiny + value
if(destiny != 11 and destiny !=22 and destiny >9):
    destiny=sum_n(destiny)
print("Your destiny number:",destiny)    
#d
print("Nhap ten cua ban:")
name_old=input()
name=name_old.upper()
soul=0;
for i in np.arange(0,len(name)):
    if(name[i]=='A' or name[i]=='Ă' or name[i]=='Â'):
        value=1
    elif(name[i]=='E' or name[i]=='Ê'):
        value=5
    elif(name[i]=='I'):
        value=9
    elif(name[i]=='O' or name[i]=='Ô' or name[i]=='Ơ'):
        value=6
    elif(name[i]=='U' or name[i]=='Ư'):
        value=3
    elif(name[i]=='Y' and name[i-1] !='U' and name[i+1]!='U' and name[i-1]!='Ư' and name[i+1]!='Ư'):
        value=7
    else:
        value=0
    soul=soul+value
if(soul >11):
    soul=sum_n(soul)
print("Your soul number is:",soul)   
#e
impression=0;
for i in np.arange(0,len(name)):
    if(name[i] == 'J' or name[i] == 'S'):
        value=1
    elif(name[i] == 'B' or name[i] == 'K' or name[i] == 'T'):
        value=2
    elif(name[i] == 'C' or name[i] == 'L'):
        value=3
    elif(name[i] == 'D' or name[i] == 'M' or name[i] == 'V'):
        value=4
    elif(name[i] == 'N' or name[i] == 'W'):
        value=5
    elif(name[i] == 'F' or name[i] == 'X'):
        value=6   
    elif(name[i] == 'G' or name[i] == 'P'):
        value=7
    elif(name[i] == 'H' or name[i] == 'Q' or name[i] == 'Z'):
        value=8
    elif(name[i] == 'R'):
        value=9
    elif((name[i] == 'Y' and name[i-1]=='U') or (name[i] == 'Y' and name[i+1] == 'U') or (name[i] == 'Y' and name[i-1]=='Ư') or (name[i] == 'Y' and name[i+1]=='Ư') ):
        value=9
    else:
        value=0   
    impression=impression+value    
if(impression>11):
    impression=sum_n(impression)
print("Your impession number is:",impression)

