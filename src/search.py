from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
import json
from src.gpt import qea, translate, summarize, get_keywords, summarize_in
from app.models import Historic, Ai, Function, ChatHistory, Chat
from usuario.models import Usuario

from django.shortcuts import get_object_or_404


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def search(request):
    ai = int(request.GET.get("ai"))
    type = int(request.GET.get("type"))
    data = json.loads(request.body.decode('utf-8'))

    text = data.get('text', '')
    user_id = int(data.get('user_id', ''))

    from_lang = data.get('from_lang', '')
    to_lang = data.get('to_lang', '')

    amount = data.get('amount', '')

    keyNum = data.get('keyNum', '')

    words = data.get('words', '')

    # Inicialize a variável response com um valor padrão
    response = None
    print(type, ai)


    user_instance = get_object_or_404(Usuario, id=1)
    ai_instance = get_object_or_404(Ai, id=ai)
    type_instance = get_object_or_404(Function, id=type)

    chat = Chat.objects.filter(user=user_instance)
    if ai == 1:
        if type == 1:
            response = qea(text)
            chatHistory = ChatHistory.objects.create(ai=ai_instance, function=type_instance, question=text, choice=response)
            chatHistory.chat.set(chat)
            chatHistory.save()
            print(response)
        elif type == 2:
            response = translate(text, from_lang, to_lang)
            print(response)
        elif type == 3:
            # breakpoint()
            response = summarize(text, amount)
            print(response)
        elif type == 4:
            response = get_keywords(text, keyNum)
            print(response)
        elif type == 5:
            response = summarize_in(text, words)
            print(response)

    elif ai == 2:
        print("gpt-3.5")

    Historic.objects.create(ai=ai_instance, function=type_instance, question=text, user=user_instance, choice=response)
    
    return Response({"ai": ai, "type": type, "text": text, "user_id": user_id, "response": response})