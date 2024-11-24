<template>
    <div class="signup-container" v-if="store.user">
      <h2 class="signup-title">내 정보 수정</h2>
      <form class="signup-form" @submit.prevent="handleSubmit">
        <!-- 기본 정보 -->
        <div class="input-group fixed-info-list">
          <div class="fixed-info-item">
            <p>이름</p>
            <p>{{ store.user.name }}</p>
          </div>
          <div class="fixed-info-item">
            <p>생년월일</p>
            <p>{{ store.user.birth_date }}</p>
          </div>
          <div class="fixed-info-item">
            <p>아이디</p>
            <p>{{ store.user.email }}</p>
          </div>
          <div class="fixed-info-item">
            <p>비밀번호</p>
            <!-- 비밀번호 변경 버튼 -->
            <button type="button" class="password-btn" :class="{ 'active': showPasswordFields }"
              @click="togglePasswordChange">
              {{ showPasswordFields ? '닫기' : '비밀번호 변경' }}
            </button>
          </div>
        </div>
  
  
  
        <!-- 비밀번호 변경 필드 -->
        <div v-show="showPasswordFields">
          <p>기존 비밀번호</p>
          <div class="input-group">
            <input type="password" class="input-field" placeholder="기존 비밀번호를 입력하세요" v-model="pwFormData.old_password">
          </div>
  
          <p>새로운 비밀번호</p>
          <div class="input-group-newpw">
            <input type="password" class="input-field" placeholder="새로운 비밀번호를 입력하세요" v-model="pwFormData.new_password1">
            <p class="password-require">* 비밀번호는 대소 문자, 특수문자를 포함한 8자리 이상으로 설정해주세요</p>
          </div>
  
          <p>새로운 비밀번호 확인</p>
          <div class="input-group">
            <input type="password" class="input-field" placeholder="새로운 비밀번호를 한번 더 입력해주세요"
              v-model="pwFormData.new_password2">
          </div>
        </div>
  
        <p>자산</p>
        <div class="input-group">
          <div class="man">
            <input type="text" class="input-field" placeholder="자산을 입력하세요" v-model="formData.asset"
              style="text-align: end; padding-right: 50px; padding-top: 10px;">
            <span class="man-won">만원</span>
            <!-- <p class="asset-min">* 만 단위 이상 기입</p> -->
          </div>
        </div>
  
        <p>저축 목표</p>
        <div class="goal-group">
          <button v-for="goal in goals" :key="goal" type="button" class="goal-btn"
            :class="{ 'active': formData.saving_purpose.includes(goal) }" @click="toggleGoal(goal)">
            {{ goalsToKor[goal] }}
          </button>
        </div>
  
        <p>저축 기간 (개월)</p>
        <div class="savings-slider-wrapper">
          <div class="savings-amount-slider">
            <input type="radio" name="savings-period" id="amount1" value="0" v-model="formData.saving_period" disabled>
            <label for="amount1" data-amount="0"></label>
            <input type="radio" name="savings-period" id="amount2" value="6" v-model="formData.saving_period">
            <label for="amount2" data-amount="6"></label>
            <input type="radio" name="savings-period" id="amount3" value="12" v-model="formData.saving_period">
            <label for="amount3" data-amount="12"></label>
            <input type="radio" name="savings-period" id="amount4" value="24" v-model="formData.saving_period">
            <label for="amount4" data-amount="24"></label>
            <input type="radio" name="savings-period" id="amount5" value="36" v-model="formData.saving_period">
            <label for="amount5" data-amount="36"></label>
          </div>
        </div>
  
        <div class="input-group">
          <div class="man">
            <p class="deb-amount">저축 금액</p>
            <input type="text" class="input-field" v-model="formData.saving_amount" placeholder="금액을 입력하세요"
              style="text-align: end; padding-right: 50px; padding-top: 10px;">
            <span class="man-won2">만원</span>
            <!-- <p class="asset-min">* 만 단위 이상 기입</p> -->
          </div>
        </div>
        <button type="submit" class="submit-btn">완료</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useUserStore } from '@/stores/user';
  import router from '@/router';
  
  const store = useUserStore();
  const selectedGoals = ref([]);
  const showPasswordFields = ref(false);
  const pwFormData = ref({
    old_password: '',
    new_password1: '',
    new_password2: '',
  });
  const formData = ref({
    asset: '',
    saving_purpose: [],
    saving_amount: '',
    saving_period: ''
  });
  
  const togglePasswordChange = (event) => {
    event.preventDefault();
    showPasswordFields.value = !showPasswordFields.value;
    if (!showPasswordFields.value) {
      pwFormData.value.old_password = '';
      pwFormData.value.new_password1 = '';
      pwFormData.value.new_password2 = '';
    }
  };
  
  const toggleGoal = (goal) => {
    const index = selectedGoals.value.indexOf(goal);
    if (index > -1) {
      selectedGoals.value.splice(index, 1);
    } else {
      if (selectedGoals.value.length >= 3) {
        alert('목표 설정은 최대 3개까지만 가능합니다.');
        return;
      }
      selectedGoals.value.push(goal);
    }
    formData.value.saving_purpose = [...selectedGoals.value];
  };
  
  const goals = [
    'home', 'education', 'medication', 'wedding', 'future', 'seedmoney', 'travel', 'wishlist'
  ];
  
  const goalsToKor = {
    'home': '내집마련',
    'education': '교육비',
    'medication': '의료비',
    'wedding': '결혼자금',
    'future': '노후자금',
    'seedmoney': '시드머니',
    'travel': '여행자금',
    'wishlist': '위시리스트'
  };
  
  // 수정된 비밀번호 유효성 검사 함수
  const validatePassword = (password) => {
  const hasUpperCase = /[A-Z]/.test(password);
  const hasLowerCase = /[a-z]/.test(password);
  const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);
  const isLongEnough = password.length >= 8;
  console.log(hasUpperCase, hasLowerCase,  hasSpecialChar, isLongEnough)

  return isLongEnough && (hasUpperCase || hasLowerCase) && hasSpecialChar;
};
  const handleSubmit = () => {
    const updateData = {};
    const updatePwData = {};
  
    if (showPasswordFields.value && pwFormData.value.new_password1) {
      if (pwFormData.value.new_password1 !== pwFormData.value.new_password2) {
        alert('새 비밀번호가 확인용 비밀번호와 서로 다릅니다.');
        return;
      }
  
      if (!validatePassword(pwFormData.value.new_password1)) {
        alert('비밀번호는 8자 이상이며, 영문 대소문자, 숫자, 특수문자를 포함해야 합니다.');
        return;
      }
  
      updatePwData.old_password = pwFormData.value.old_password;
      updatePwData.new_password1 = pwFormData.value.new_password1;
      updatePwData.new_password2 = pwFormData.value.new_password2;
    }
  
    if (!formData.value.asset || isNaN(formData.value.asset)) {
      alert('자산 정보를 올바르게 입력해주세요.');
      return;
    }
    updateData.asset = formData.value.asset;
  
    if (selectedGoals.value.length === 0) {
      alert('저축 목적을 선택해주세요.');
      return;
    }
    updateData.saving_purpose = selectedGoals.value;
  
    if (!formData.value.saving_amount || isNaN(formData.value.saving_amount)) {
      alert('저축 금액을 올바르게 입력해주세요.');
      return;
    }
    updateData.saving_amount = formData.value.saving_amount;
  
    if (!formData.value.saving_period || isNaN(formData.value.saving_period)) {
      alert('저축 기간을 올바르게 입력해주세요.');
      return;
    }
    updateData.saving_period = formData.value.saving_period;
  
    Promise.all([
      showPasswordFields.value && Object.keys(updatePwData).length > 0 ? store.passwordChange(updatePwData) : Promise.resolve(),
      store.updateUserInfo(updateData)
    ])
    .then(() => {
      alert('정보가 성공적으로 수정되었습니다.');
      showPasswordFields.value = false;
      store.getUserInfo(); // 사용자 정보 다시 불러오기
    })
    .catch(error => {
      console.error('정보 업데이트 실패:', error);
      alert('정보 업데이트에 실패했습니다. 다시 시도해주세요.');
    });
  };
  
  onMounted(() => {
    store.getUserInfo()
      .then(() => {
        if (store.user) {
          formData.value.asset = store.user.asset || '';
          formData.value.saving_amount = store.user.saving_amount || '';
          formData.value.saving_period = store.user.saving_period || '';
          if (store.user.saving_purpose) {
            const purposeArray = Array.isArray(store.user.saving_purpose) ? store.user.saving_purpose : [store.user.saving_purpose];
            selectedGoals.value = purposeArray.slice(0, 3);
            formData.value.saving_purpose = [...selectedGoals.value];
          }
        }
      })
      .catch(error => {
        console.error('사용자 정보 로드 실패:', error);
      });
  });
  </script>
  
  <style scoped>
  /* 컨테이너 스타일 */
  .signup-container {
    width: 100%;
    max-width: 500px;
    margin: 150px auto;
    padding: 20px;
  }
  
  .signup-title {
    color: var(--main-color);
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 40px;
  }
  
  /* 입력 필드 공통 스타일 */
  p {
    color: var(--sub-text2-color);
    margin-bottom: 8px;
    font-size: 16px;
  }
  
  .input-group {
    margin-bottom: 30px;
  }
  
  .input-group>p {
    margin: 20px 0;
  }
  
  .man {
    position: relative;
  }
  
  .man-won {
    position: absolute;
    width: 32px;
    right: 10px;
    top: 12px;
    color: #808080;
    font-size: 13px;
  }
  
  .man-won2 {
    position: absolute;
    width: 32px;
    right: 10px;
    top: 40px;
    color: #808080;
    font-size: 13px;
  }
  
  .password-require {
    font-size: 12px;
    color: var(--main-text-color);
    padding-left: 10px;
    font-weight: 350;
  }
  
  .asset-min {
    font-size: 12px;
    color: #fc8a44;
    padding-left: 10px;
    font-weight: 350;
  }
  
  .input-field {
    width: 100%;
    padding: 12px;
    border: 1px solid #E5E5E5;
    border-radius: 8px;
    font-size: 14px;
    color: var(--sub-text-bold-color);
  }
  
  .input-field::placeholder {
    color: #999;
  }
  
  /* 수정 불가능한 정보 스타일 */
  .fixed-info-item {
    display: flex;
    align-items: center;
    margin: 15px 0;
  }
  
  .fixed-info-item p:first-child {
    width: 90px;
    margin-bottom: 0;
  }
  
  .fixed-info-item p:last-child {
    margin-bottom: 0;
    font-size: 14px;
    color: var(--sub-text-color);
  }
  
  .password-btn {
    padding: 5px 10px;
    border-radius: 15px;
    color: #fff;
    background-color: var(--stroke-color);
  }
  
  .password-btn.active {
    background: var(--main-text-color);
    color: white;
  }
  
  /* 생년월일 선택 스타일 */
  .birth-select-group {
    display: flex;
    gap: 10px;
    margin-bottom: 30px;
  }
  
  .select-box {
    flex: 1;
    padding: 12px;
    border: 1px solid #E5E5E5;
    border-radius: 8px;
    background: white;
    font-size: 14px;
  }
  
  /* 이메일 입력 스타일 */
  .email-input-group {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 30px;
  }
  
  .email-input-group .input-field {
    flex: 1;
  }
  
  .email-input-group span {
    color: #666;
  }
  
  /* 목표 버튼 스타일 */
  .goal-group {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 30px;
    justify-content: center;
    padding: 0 10px;
  }
  
  .goal-btn {
    width: 100px;
    padding: 12px 0;
    border: 1px solid #E5E5E5;
    border-radius: 8px;
    background: white;
    cursor: pointer;
    font-size: 13px;
    transition: all 0.3s ease;
    text-align: center;
    color: var(--sub-text-bold-color);
  }
  
  .goal-btn:hover {
    border-color: var(--main-text-color);
    color: var(--main-text-color);
  }
  
  .goal-btn.active {
    background: var(--main-text-color);
    color: white;
    border-color: var(--main-text-color);
  }
  
  /* 슬라이더 스타일 */
  .savings-slider-wrapper {
    margin: 40px 0;
  }
  
  .savings-amount-slider {
    display: flex;
    flex-direction: row;
    align-content: stretch;
    position: relative;
    width: 100%;
    height: 40px;
    user-select: none;
  }
  
  .savings-amount-slider::before {
    content: " ";
    position: absolute;
    height: 2px;
    width: 80%;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: #E5E5E5;
  }
  
  .savings-amount-slider input {
    display: none;
  }
  
  .savings-amount-slider label {
    display: inline-block;
    position: relative;
    width: 20%;
    height: 100%;
    cursor: pointer;
    color: var(--sub-text-bold-color);
  }
  
  .savings-amount-slider label::before {
    content: attr(data-amount);
    position: absolute;
    left: 50%;
    padding-top: 10px;
    transform: translate(-50%, 45px);
    font-size: 14px;
    opacity: 0.85;
    transition: all 0.15s ease-in-out;
  }
  
  .savings-amount-slider label::after {
    content: " ";
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 15px;
    height: 15px;
    border: 2px solid #E5E5E5;
    background: white;
    border-radius: 50%;
    transition: all 0.15s ease-in-out;
  }
  
  .savings-amount-slider label:hover::after {
    border-color: var(--main-color);
    background: var(--main-color);
    transform: translate(-50%, -50%) scale(1.25);
  }
  
  .savings-amount-slider input:checked+label::after {
    border-color: var(--main-color);
    background: var(--main-color);
    transform: translate(-50%, -50%) scale(0.75);
  }
  
  /* 제출 버튼 스타일 */
  .submit-btn {
    width: 100%;
    padding: 15px;
    background-color: var(--point-color);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin-top: 10px;
  }
  
  .submit-btn:hover {
    background: var(--main-color);
  }
  
  .deb-amount {
    margin-top: 90px;
    margin-bottom: 10px;
  }
  </style>