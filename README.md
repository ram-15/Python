# Python

---
import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

public class JSoupDemo {

	public static void main(String[] args)throws IOException {
		// TODO Auto-generated method stub
		Document d = Jsoup.connect("https://www.amazon.in/Apple-iPhone-Space-Grey-Storage/dp/B072LPF91D/ref=br_msw_pdt-1?_encoding=UTF8&smid=A14CZOWI0VEHLG&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=KBJ7DAY2BH1JDA3PCJ4C&pf_rd_t=36701&pf_rd_p=ba94e3ba-51a5-4848-b49d-0f067cfce50e&pf_rd_i=desktop").timeout(6000).get();
		System.out.println(d.title());
		//System.out.println(d);
		//Elements ele = d.select("div#altImages > ul > li");
		//System.out.println(ele);
		//Elements ele1 = d.select("li.a-spacing-small item");
		//Elements ele1 = ele.select("ul.a-unordered-list a-nostyle a-button-list a-vertical a-spacing-top-micro");
		//Elements ele = d.select("div#feature-bullets > ul > li");
		//Elements el1 = d.select("li.a-list-item");
		Elements imageElement = d.select("div#altImages > ul");
		//class="a-spacing-small item imageThumbnail a-declarative"
		System.out.println(imageElement);
		/*for(int i=0; i<ele.size(); i++ ){
			Elements ele1 = d.select("span.a-list-item");
			System.out.println(ele1);
		}*/
	}

}
