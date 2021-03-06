#include <iostream>

int main() {
    std::cout << "電神看著你狂妄地笑著，心想著又有一個店小二來送菜了。現在他的助手突然帶著重要的訊息前來，他不想讓你聽到內容，但你擋在電神面前，以致於助手無法傳遞訊息。於是，他決定使用「雜湊」來產生一串你聽不懂的數字，再請電神用已經講好的方法來解密。問題是，雜湊並非一個簡單的技巧，而助手因為不夠電而忘了如何雜湊，所以他對你提出一個條件：如果你幫他雜湊並把訊息傳遞給電神，則你會知道訊息的所有內容。好奇的你心想，這是什麼簡單的東西，雜湊我幼稚園就會了！現在請你找到兩個好的常數雜湊該訊息，讓電神解密時不會發生碰撞或其他錯誤。\n";
    std::cout << "以下 h 為雜湊值、p、m 為常數、a[i] 為訊息串的一個字母。雜湊式為 h[i + 1] = (h[i] * p + a[i]) % m。請問下列哪一項是一個好的雜湊方法？\n";
    std::cout << "1. p = 0, m = 1\n";
    std::cout << "2. p = 1, m = 0\n";
    std::cout << "3. p = 1560, m = 1563\n";
    std::cout << "4. p = 1570, m = 1576\n";
    std::cout << "5. p = 1559, m = 1581\n";
    std::cout << "6. p = 1567, m = 1571\n";
    std::cout << "7. 開玩笑的，幼稚園怎麼可能會這種東西，我開玩笑的啦，放我一馬\n";
    int choice;
    std::cin >> choice;
    if (choice == 6) std::cout << "助手用欽慕的眼神望著你，開始對著你瘋狂地膜拜，但此舉卻惹怒了在一旁的電神。電神怒吼：「你這個沒用的東西，上禮拜社課才剛教完的東西，現在就忘記！？還要請一個外人來幫忙！？我看你是沒救了，快給我從電算社滾出去！」接著發射一道超強的電流，直接一擊斃命，把他的助手電爛了。電神上下打量著你，竟然能解出這種難題，不過後來想一想，你肯定是靠賽嘛，怎麼可能有人會這種困難的知識！電神又露出了他詭異唯妙的笑容......\n";
    else if (choice <= 7 && choice >= 1) std::cout << "電神先是冷笑一聲，緊接著是更加狂妄的大笑：「哼哈哈哈哈你答錯囉，準備接受電神的制裁和助手的怒火吧！」\n";
    else std::cout << "欸欸欸幹什麼東西！連選項數字都不會看的嗎！憑你這實力還想挑戰電神？乖乖重選！\n\n";
    system("pause");
	return 0;
}
