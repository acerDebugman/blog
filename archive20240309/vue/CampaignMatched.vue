<template>
  <el-row>
    CampaignMatched
    <el-input v-model="firstName"></el-input>
    <div>fullName: {{ fullName }}</div>
    <div v-bind:class="classObj">watch: {{ watchName }}</div>
    <div><el-button type="primary" @click="showFullName">clickMe</el-button></div>
    <template v-if="Math.random() > 0.5">
      <h1>kkk</h1>
      <div>joe zhang kkk</div>
    </template>
    <template v-else>
      <h2>aaaa</h2>
    </template>
  </el-row>
</template>
<script>
  import ElButton from "../../../node_modules/element-ui/packages/button/src/button.vue";
  var _ = require('lodash');

  export default {
    components: {ElButton},
    name: "CampaignMatched",
    data() {
      return {
        firstName: "joe",
        lastName: "zhang",
        watchName: "watchNmae",
        isActive: false,
      }
    },
    mounted() {
      console.log("in goods manage")
    },
    methods: {
      joe: function() {

      },
      showFullName: _.debounce(
        function() {
          console.log("full name")
          let arr = [1]
          let _other = _.concat(arr, [2])
          console.log(_other)

          this.isActive = !this.isActive
        },
        100
      )
    },
    computed :{
      fullName: function() {
        return this.firstName + " " + this.lastName
      },
      classObj: function() {
        return {
          jactive: this.isActive,
          jheight: this.isActive
        }
      }
    },
    watch: {
      firstName: function() {
        this.watchName = this.firstName + this.lastName
      }
    }
  }

</script>
<style>
  .jactive {
    color: #f00;
  }
  .jheight {
    line-height: 50px;
  }
</style>
