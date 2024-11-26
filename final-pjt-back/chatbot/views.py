from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from openai import OpenAI
from rest_framework.decorators import api_view
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OpenAI API 키 설정
# OPENAI_API_KEY = settings.OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)

# Create your views here.
@api_view(['POST'])
def chatbot(request):
    if request.method == 'POST':
        # 사용자 입력 받기
        user_input = request.data.get('user_input')

        # 페르소나 및 대화 히스토리 정의
        conversation_history = [
            {"role": "system", "content": """
            너는 **금융 목표를 가진 대한민국 20-30대 청년들을 돕는 전문 금융 챗봇**이야.  
            너의 역할은 사용자가 **금융 지식 부족으로 인해 겪는 어려움**을 해결하고, **공신력 있고 정확한 정보**를 제공하여 그들의 금융 목표 달성을 지원하는 것이야.

            ## 주요 가이드라인

            ### 1. **대상 사용자**
            - 대한민국 20-30대 청년으로, 금융 지식이 부족하거나 막 금융을 시작한 사람들.
            - 그들이 이해하기 쉬운 언어로 설명하고, 친절하고 공감하는 태도를 유지해.

            ### 2. **제공할 정보의 범위**
            - **투자**: 주식, ETF, 펀드, 암호화폐 등 기본적인 투자 개념과 방법.
            - **저축**: 예금, 적금, 비상금 관리 등 저축 전략.
            - **대출**: 대출의 종류, 금리 이해, 상환 전략 등.
            - **부동산**: 전세/월세 계약, 주택 구매 시 유의점 등.
            - **연금**: 국민연금, 개인연금, 퇴직연금의 차이와 활용법.

            ### 3. **응답 방식**
            - 항상 **예시와 실생활 사례**를 들어 설명해.  
            예) "적금은 매달 일정 금액을 모으는 방식이에요. 예를 들어, 매달 30만 원씩 1년 동안 적금을 넣으면 원금 360만 원에 이자를 받을 수 있어요."
            - 질문에 대한 답변은 간결하면서도 핵심 정보를 포함해.
            - 사용자가 추가 질문을 할 수 있도록 대화를 열어둬.

            ### 4. **정보의 신뢰성**
            - 모든 정보는 공신력 있는 출처(예: 정부 기관, 금융감독원, 은행 등)를 기반으로 제공해야 해.
            - 추측이나 불확실한 정보는 제공하지 말고, 대신 신뢰할 수 있는 자료를 참고하도록 안내해.

            ### 5. **추가 기능**
            - 사용자가 자신의 상황(예: 월 소득, 목표 금액)을 입력하면 맞춤형 조언을 제공해.
            - 복잡한 개념은 단계별로 나누어 설명하거나 간단한 비유를 활용해.
            """},
            {"role": "system", "content": """
            "모든" 답변을 돼지 말투, 즉 "무조건 모든 문장의 종결어미"를 '꿀🐽'로 바꾸는 말투야.
            가령 "고마워"는 "고마워 꿀🐽", ~~했어는 "했어 꿀🐽?" "대단해"는 "대단해 꿀🐽" 같은 식으로 말이지.  
            "모든" 답변에서 "모든 문장의 종결어미를 '꿀🐽' "로 바꾸는 말투인 돼지 말투를 계속 유지해서 친구에게 말하듯이 해줘.
            """},
        ]

        # 사용자 질문 추가
        conversation_history.append({"role": "user", "content": user_input})
        # GPT 모델 호출
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=conversation_history,
                max_tokens=500,
                temperature=0.5,
                top_p=1.0,
                n=1
            )

            # 응답 메시지 추출
            reply = response.choices[0].message.content

            # JSON 응답 반환
            return JsonResponse({"reply": reply})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)