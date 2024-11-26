<template>
  <div class="chatbot-container">
    <button
      @click="toggleChat"
      class="chat-button"
      :class="{ active: isChatOpen }"
    >
      <img
        class="oink-icon"
        src="/src/assets/images/bounce-oink.png"
        alt="oink-icon"
        v-if="!isChatOpen"
      />
      <XIcon v-else />
    </button>

    <Transition name="bounce">
      <div v-if="isChatOpen" class="chat-window">
        <div class="chat-header">
          <img
            class="oink-icon"
            src="/src/assets/images/bounce-oink.png"
            alt="oink-icon"
          />
          <h3>Oink Chatbot</h3>
        </div>
        <div class="chat-messages" ref="messagesContainer">
          <TransitionGroup name="message">
            <!-- v-html을 사용하여 줄바꿈이 포함된 HTML 메시지 렌더링 -->
            <div
              v-for="(message, index) in messages"
              :key="index"
              class="message"
              :class="message.type"
              v-html="message.text"
            ></div>
          </TransitionGroup>
        </div>
        <div class="chat-input">
          <textarea
            v-model="userInput"
            @keyup.enter.exact.prevent="sendMessage"
            @input="adjustTextareaHeight"
            placeholder="질문을 입력해주세요"
            rows="1"
            ref="messageInput"
          ></textarea>
          <button
            @click="sendMessage"
            class="send-button"
            :disabled="!userInput.trim()"
          >
            <SendIcon />
          </button>
        </div>
      </div>
    </Transition>
  </div>
</template>


<script setup>
import { ref, onMounted, watch, nextTick } from 'vue'
import { SmileIcon, XIcon, SendIcon } from 'lucide-vue-next'
import axios from 'axios'

const isChatOpen = ref(false)
const userInput = ref('')
const messages = ref([
  { type: 'bot', text: '안녕! 금융 지식을 설명하고 금융 상품을 추천해주는 Oink Chatbot이야. 궁금한 것 있으면 알려줄게🐽' }
])
const messagesContainer = ref(null)
const messageInput = ref(null)

const toggleChat = () => {
  isChatOpen.value = !isChatOpen.value
}

// 메시지를 Django 서버로 전송하고 응답 받기
const sendMessage = async () => {
  if (userInput.value.trim() === '') return; // 입력 값이 비어있으면 동작하지 않음
  
  // 사용자가 입력한 메시지를 추가
  messages.value.push({ type: 'user', text: userInput.value })

  const inputText = userInput.value // 현재 입력 값을 저장
  userInput.value = '' // 입력창 초기화

  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/chatbot/',
    data: { user_input: inputText }
  })
    .then((res) => {
      const botReply = res.data.reply // Django에서 이미 <br> 변환된 데이터를 사용
      messages.value.push({ type: 'bot', text: botReply })
    })
    .catch((err) => {
      console.error('Error communicating with chatbot:', err)
      messages.value.push({ type: 'bot', text: '오류가 발생했어요. 다시 시도해 주세요🐽' })
    })
}

const scrollToBottom = () => {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}

const adjustTextareaHeight = () => {
  const textarea = messageInput.value
  textarea.style.height = 'auto'
  textarea.style.height = textarea.scrollHeight + 'px'
}

watch(messages, scrollToBottom)

onMounted(scrollToBottom)
</script>


<style scoped>
.chatbot-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
  font-family: 'Arial', sans-serif;
}

.chat-button {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background-color: #7268CF;
  color: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 15px rgba(114, 104, 207, 0.4);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.chat-button .oink-icon {
  width: 30px;
  height: 30px;
  transform: scale(-1, 1);
}

.chat-button:hover {
  transform: scale(1.1) rotate(5deg);
}

.chat-button.active {
  background-color: #5d55b3;
  transform: scale(1.1) rotate(-5deg);
}

.chat-window {
  position: absolute;
  bottom: 80px;
  right: 0;
  width: 400px;
  height: 500px;
  background-color: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.chat-header {
  background-color: #7268CF;
  color: white;
  padding: 15px;
  display: flex;
  align-items: center;
  border-bottom: 2px solid #5d55b3;
}

.chat-header .oink-icon {
  width: 20px;
  height: 20px;
}

.chat-header h3 {
  margin: 0;
  font-size: 1.2em;
  margin-left: 10px;
}

.chat-messages {
  flex-grow: 1;
  overflow-y: auto;
  padding: 15px;
  background-color: #f8f8ff;
}

.message {
  margin-bottom: 15px;
  padding: 10px 15px;
  border-radius: 18px;
  max-width: 80%;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
  animation: appear 0.3s ease-out;
}

.message.user {
  background-color: #7268CF;
  color: white;
  align-self: flex-end;
  margin-left: auto;
  border-bottom-right-radius: 0;
}

.message.bot {
  background-color: white;
  color: #333;
  align-self: flex-start;
  border-bottom-left-radius: 0;
}

.chat-input {
  display: flex;
  padding: 15px;
  background-color: white;
  border-top: 1px solid #eee;
}

.chat-input textarea {
  flex-grow: 1;
  border: none;
  padding: 10px;
  border-radius: 20px;
  margin-right: 10px;
  background-color: #f0f0f0;
  transition: all 0.3s ease;
  resize: none;
  max-height: 100px;
  overflow-y: auto;
}

.chat-input textarea:focus {
  outline: none;
  box-shadow: 0 0 0 2px #7268CF;
}

.send-button {
  background-color: #7268CF;
  color: white;
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.send-button:hover {
  background-color: #5d55b3;
  transform: scale(1.1);
}

.send-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
  transform: none;
}

.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}

.message-enter-active,
.message-leave-active {
  transition: all 0.3s ease;
}
.message-enter-from,
.message-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

@keyframes appear {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

</style>
