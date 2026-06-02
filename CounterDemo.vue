<template>
    <div class="counter-box">
        <h2>
        计算器练习
        </h2>
    <!--1.显示数字-->
    <div class="number">{{ count }}</div>

    <!--2.操作按钮-->
    <div class="buttons">
        <button @click="decrease" class="btn red">减少-</button>
        <button @click="reset" class="btn gray">重置</button>
        <button @click="increase" class="btn green">增加</button> 

    </div>

    <!--3.动态样式演示(当数字大于0时变绿)-->
    <p :class="{'status-text':true,'positive':count>0,'negative':count<0}">
        当前状态:{{ statusMessage }}
    </p>
    </div>
</template>

<script setup>
 import { ref,computed } from 'vue';

 //定义一个响应式变量,初始值为0
 const count =ref(0);

 //定义增加的方法
 const increase =()=>{
    count.value++ //注意:在script中修改ref需要加.value
 }

 //定义减少的方法
 const decrease =()=>{
    // const.value--;
    count.value--;
 }

 //定义重置的方法
 const reset =()=>{
 count.value =0
 }

 //计算属性,根据count的值自动返回不同的文字
 const statusMessage = computed(() =>{
    if(count.value >0) return'正数'
    if(count.value<0) return'负数'
    return '零'
 })


</script>


<style scoped>
  /* 给这个组件加上一点样式,让它好看点 */
.counter-box{
    border: 2px dashed #42b983;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    max-width: 400px;
    margin: 20px auto;
    font-family: sans-serif;

}

.number{
   font-size: 60px;
   font-weight: bold;
   color: #2c3e50;
   margin: 20px 0; 
}

.bottons{
    display: flex;
    justify-content: center;
    gap: 10px;
}

.btn{
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    color:white;
    font-size: 16px;
    transition: transform 0.1s;

}

.btn:active{
   transform: scale(0.95); 
}

.green{background-color: #42b983;}
.red{background-color: #ff5e57;}
.gray{background-color:#95a5a6;}


.status-text{
    margin-top: 20px;
    font-weight: bold;
}

.positive{color: #42b983;}
.negative{color: #ff5e57}
 
</style>