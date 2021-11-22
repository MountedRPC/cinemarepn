//controls for carousel
function carouselSwitch(d, t){
    $('.carousel-card-image',$(t).parents('.carousel-card')).carousel(d);
    $('.carousel-contents',$(t).parents('.carousel-card')).carousel(d);
  }
  $('.next-btn').click(function(){
    carouselSwitch('next', this)
  })
  $('.prev-btn').click(function(){
    carouselSwitch('prev', this)
  })
  //shorter for text
  let text = [];
  let textSmall = [];
  const x=$('.card-text').toArray();
  for (const p in x) {
    text[p] = x[p].innerText;
    let i;
    for(i = 50; i<text[p].length; i++){
      if(text[p][i]==' '){break;}
    }
    textSmall[p] = text[p].slice(0, i)+'[...]';
  }
  function smol(){
    for (const p in x) {
      x[p].innerText = textSmall[p];
    }
  }
  function big(){
    for (const p in x) {
      x[p].innerText = text[p];
    }
  }
  $(window).resize(function() {
  size()
  });
  size();
  function size(){
      var width = $(window).width();
    if (width > 1250 || width < 992){
      big();
    }else{
      smol();
    }
  }
  //loader
  class Loader{
    constructor(c){
        this.c=c;
        this.ctx = c.getContext("2d");
        this.time =  parseInt(c.dataset.interval);
        this.speed=20;
        this.t=0;
        this.lw = c.width/4
        this.l = setInterval(this.draw.bind(this), this.speed)
    }
        draw(){
          this.ctx.clearRect(0, 0, this.c.width, this.c.height)
          if(!$(this.c).hasClass('paused')){
            this.t+=this.speed;
          }
          if(this.t>this.time){
            if(this.c.dataset.repeat!='1' && this.c.dataset.repeat!='true'){clearInterval(this.l)}
            this.t=0;
            eval(this.c.dataset.function)
          }
          this.ctx.beginPath()
          this.ctx.arc(this.c.width/2, this.c.height/2, this.c.width/2-this.lw/2, 1.5*Math.PI, this.t/this.time*2*Math.PI+1.5*Math.PI)
          this.ctx.lineWidth=this.lw
          this.ctx.strokeStyle=this.c.dataset.color;
          this.ctx.stroke()
          this.ctx.closePath()
        }
  }
  let loaders = $('.loader').toArray()
  for(i in loaders){
    new Loader(loaders[i])
  }
  //pause for loader
  var p=0;
  $('.carousel-card').mouseenter(function (){
    $('.loader', this).addClass('paused')
    
  })
  
  $('.carousel-card').mouseleave(function (){
    $('.loader', this).removeClass('paused')
  })




  (function ($) {
    "use strict";
    // Auto-scroll
    $('#myCarousel').carousel({
      interval: 5000
    });
  
    // Control buttons
    $('.next').click(function () {
      $('.carousel').carousel('next');
      return false;
    });
    $('.prev').click(function () {
      $('.carousel').carousel('prev');
      return false;
    });
  
    // On carousel scroll
    $("#myCarousel").on("slide.bs.carousel", function (e) {
      var $e = $(e.relatedTarget);
      var idx = $e.index();
      var itemsPerSlide = 3;
      var totalItems = $(".carousel-item").length;
      if (idx >= totalItems - (itemsPerSlide - 1)) {
        var it = itemsPerSlide -
            (totalItems - idx);
        for (var i = 0; i < it; i++) {
          // append slides to end 
          if (e.direction == "left") {
            $(
              ".carousel-item").eq(i).appendTo(".carousel-inner");
          } else {
            $(".carousel-item").eq(0).appendTo(".carousel-inner");
          }
        }
      }
    });
  })
  (jQuery);