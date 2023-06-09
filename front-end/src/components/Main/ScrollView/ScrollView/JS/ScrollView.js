import ScrollSwitch from "../../ScrollSwitch/JS/ScrollSwitch";

import "../CSS/ScrollView.css"

function ScrollView(){
  const scrollSwitches = getScrollSwitches()
  const contentBlocks = document.getElementsByClassName("content-block");
  const switchButtons = document.getElementsByClassName("scroll-view__switcher__switch");

  let activeNum = 0
  let canMove = true
  let activeNumTimer = 1000

  let x1 = null;
  let y1 = null;

  function init(){
    catchWheel()
    catchTouch()
  }

  function catchWheel(){
    if (window.addEventListener) { 
      if ('onwheel' in document) { 
        window.addEventListener("wheel", onWheelHandler); 
      } else if ('onmousewheel' in document) { 
        window.addEventListener("mousewheel", onWheelHandler); 
      } else {
        window.addEventListener("MozMousePixelScroll", onWheelHandler); } 
    } else { 
      window.attachEvent("onmousewheel", onWheelHandler); 
    } 
  }

  function onWheelHandler(e) {
    if(canMove){
      e = e || window.event;  
      let delta = e.deltaY || e.detail || e.wheelDelta;  
      delta>0 ? changeActiveNum(true) : changeActiveNum();
    }
  }

  function catchTouch(){
    document.addEventListener('touchstart', touchStartHandler, false);
    document.addEventListener('touchmove', touchMoveHandler, false);
  }

  function touchStartHandler(event) {
    let firstTouch = event.touches[0];
    x1 = firstTouch.clientX;
    y1 = firstTouch.clientY;
  }

  function touchMoveHandler(event) {
    if (!x1 || !y1) {
      return false;
    }
    let x2 = event.touches[0].clientX;
    let y2 = event.touches[0].clientY;

    let xDiff = x2 - x1;
    let yDiff = y2 - y1;

    if (Math.abs(xDiff) < Math.abs(yDiff)) {
      changeActiveNum(yDiff < 0)
    }
  }
  
  function switchByClickHandler(num){
    if(activeNum!==num){
      changeActiveNum(activeNum<num,num)
    }
  } 

  function moveContentBlock(move){
    let timer = setInterval(()=>{
      activeNumTimer += 100
      if(activeNumTimer === 1000){
        canMove = true
        clearInterval(timer)
      }
    },100)

    switchScrollButtons(move)

    for (let i = 0; i < contentBlocks.length; i++) {
      contentBlocks[i].style.transform = `translateY(-${activeNum*100}%)`
    }
  }

  function switchScrollButtons(move){
    for (let i = 0; i < switchButtons.length; i++) {
      if(!switchButtons[i].classList.contains("switch_overflow")){
        switchButtons[i].querySelector("img").classList.remove("switch__image_hold");

        if(move){ switchButtons[i].querySelector("img").classList.add("switch__image_hide") } 
        else {    switchButtons[i].querySelector("img").classList.add("switch__image_reverse-hide") }

        setTimeout(()=>{switchButtons[i].classList.add("switch_overflow")},200);

        if(move){ setTimeout(()=>{switchButtons[i].querySelector("img").classList.remove("switch__image_hide")},1000) } 
        else {    setTimeout(()=>{switchButtons[i].querySelector("img").classList.remove("switch__image_reverse-hide")},1000) }
      }

      let switchNumber = switchButtons[i].getAttribute("switch-number");
      if(+switchNumber === activeNum){
        setTimeout(()=>{
          if(move){ switchButtons[i].querySelector("img").classList.add("switch__image_show") } 
          else {    switchButtons[i].querySelector("img").classList.add("switch__image_reverse-show") }
        },400)

        setTimeout(()=>{switchButtons[i].classList.remove("switch_overflow")},650)

        setTimeout(()=>{
          if(move){ switchButtons[i].querySelector("img").classList.remove("switch__image_show") } 
          else {    switchButtons[i].querySelector("img").classList.remove("switch__image_reverse-show") }

          switchButtons[i].querySelector("img").classList.add("switch__image_hold");
        },900)
      }
    }
  }

  function changeActiveNum(move,page){
    if(!isNaN(page) && canMove){
      activeNum = page;
      moveContentBlock(move);
      canMove = false;
      activeNumTimer = 0;
    } else {
      if(move && activeNum < contentBlocks.length - 1 && canMove){
        activeNum++;
        moveContentBlock(move);
        canMove = false;
        activeNumTimer = 0;
      } else if(!move && activeNum > 0 && canMove) {
        activeNum--;
        moveContentBlock(move);
        canMove = false;
        activeNumTimer = 0;
      }
    }
  }

  function getScrollSwitches(){
    let scrollSwitches = []

    for (let i = 0; i < 3; i++) {
      if(i===0){
        scrollSwitches.push(
          <ScrollSwitch 
            onClick={switchByClickHandler} 
            imageClassName='switch__image_hold'
            key={i} 
            id={i}
          />
        )
      } else {
        scrollSwitches.push(
          <ScrollSwitch 
            onClick={switchByClickHandler} 
            className="switch_overflow"
            key={i} 
            id={i}
          />
        )
      }
    }

    return scrollSwitches
  }

  init()
  
  return (
    <div className="scroll-view">
      <ul className="scroll-view__switcher">
        {scrollSwitches}
      </ul>
    </div>
  );
}

export default ScrollView;