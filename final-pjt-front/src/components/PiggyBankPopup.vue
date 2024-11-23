 <template>
  <div class="piggybank-popup-container">
    <div class="piggybank-popup">
      <div class="piggybank-join">
        <div class="piggybank-join-btns">
          <div class="piggybank-join-btn">
            <p>새로운 걸로 할게요!</p>
            <p><span>username</span>님께 맞는 예적금 상품을 추천받고
              <br>새로운 예적금을 만들어보세요!</p>
          </div>
          <div class="piggybank-join-btn">
            <p>연동된 계좌로 할게요!</p>
            <p><span>username</span>님의 기존 예적금 상품으로
              <br>돼지 저금통을 만들어보세요!</p>
          </div>
        </div>
        <button>다음에 만들기</button>
      </div>
      <div class="piggybank-join-info">
        <div class="piggybank-img">
          <span class="piggy-nickname-btn">저금통 애칭</span>
          <p class="piggy-nickname"></p>
          <div class="piggybank-img">
          <img src="@/assets/images/pink-pig(25).png" alt="pink-pig-img">
          <span ref="weightDisplay" class="weight">{{ curWeight }}kg</span>
          <div class="progress-outer">
            <div class="progress-container">
              <div class="progress-bar" ref="progressBar"></div>
              <div class="indicator-wrapper" ref="indicatorWrapper">
                <img class="progress-indicator" src="@/assets/images/indicator.png" alt="indicator-img">
              </div>
            </div>
          </div>
        </div>
        </div>
        <form>
          <div class="piggybank-input">
            <label for="piggybank-name">돼지 저금통 이름</label>
            <input type="text" id="piggybank-name" placeholder="저금통 이름을 입력하세요">
          </div>
          <div class="piggybank-input">
            <label for="piggybank-account">예적금 선택</label>
            <select name="" id="">
              <option value=""></option>
            </select>
          </div>
        </form>
      </div>
    </div>
  </div>
 </template>
 
 <script setup>
 
 </script>
 
 <style scoped>
 
 </style>