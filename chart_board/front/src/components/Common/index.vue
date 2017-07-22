<template>
  <div class="comp-common">
    <left-menu></left-menu>
    <div class="right-panel-wrap">
      <top-nav></top-nav>
      <bread-crumb></bread-crumb>
      <slot>??</slot>
    </div>
  </div>
</template>

<script type="text/javascript">
  import leftMenu from './Menu/';
  import topNav from './Nav/';
  import breadCrumb from './Breadcrumb/';
  import './index.scss';

  export default {
    // data() {},
    // created() {},
    // mounted() {},
    // updated() {},
    // beforeDestory() {},

    components: {
      leftMenu,
      topNav,
      breadCrumb,
    },
  }
</script>