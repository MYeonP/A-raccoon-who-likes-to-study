package sungJuk;

import java.util.ArrayList;

public class SungJukList implements SungJuk {

	@Override
	public void execute(ArrayList<SungJukDTO> sungJukDTO) {
        System.out.println();

        System.out.println("번호\t\t이름\t\t국어\t\t영어\t\t수학\t\t총점\t\t평균");

//        for (int i = 0; i < scoreDTOS.size(); i++) { // ArrayList의 크기: size()
////            System.out.println(scoreDTOS.get(i)); // 주소값:
//            System.out.printf("%d\t%s\t%d\t%d\t%d\t%d\t%f\t\n",
//                    scoreDTOS.get(i).getNumber(),
//                    scoreDTOS.get(i).getName(),
//                    scoreDTOS.get(i).getKor(),
//                    scoreDTOS.get(i).getEng(),
//                    scoreDTOS.get(i).getMath(),
//                    scoreDTOS.get(i).getTotal(),
//                    scoreDTOS.get(i).getAvg());
//        }

//        for (ScoreDTO dto : scoreDTOS) {
//            System.out.printf("%d\t%s\t%d\t%d\t%d\t%d\t%f\t\n",
//                    dto.getNumber(),
//                    dto.getName(),
//                    dto.getKor(),
//                    dto.getEng(),
//                    dto.getMath(),
//                    dto.getTotal(),
//                    dto.getAvg());
//        }

        for (SungJukDTO dto : sungJukDTO) {
            System.out.println(dto);// toString()이 생략되어있어 @클래스명16진수로 출력될 수 있게 함 -> override하여 format 변경
        }
    }
}