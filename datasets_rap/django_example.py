# models.py

from django.db import models

class BotConversation(models.Model):
    user_input = models.CharField(max_length=255)
    bot_response = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_input

# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import BotConversation

def bot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        bot_response = generate_response(user_input)  # generate_response is a function that uses an NLP library to generate a response
        conversation = BotConversation(user_input=user_input, bot_response=bot_response)
        conversation.save()

        data = {
            'bot_response': bot_response
        }
        return JsonResponse(data)

    return render(request, 'bot.html')

# bot.html

<form id="bot-form">
  <input type="text" id="user-input">
  <button type="submit">Send</button>
</form>

<div id="bot-response"></div>

<script>
  $(document).ready(function() {
    $('#bot-form').submit(function(e) {
      e.preventDefault();
      $.ajax({
        url: '{% url "bot" %}',
        type: 'POST',
        data: {
          'user_input': $('#user-input').val(),
          'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(data) {
          $('#bot-response').text(data.bot_response);
        }
      });
    });
  });
</script>
