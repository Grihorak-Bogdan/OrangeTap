import "../CSS/ScrollSwitch.css"

function ScrollSwitch(props){
  const data = {
    id:             props.id,
    catchClick:     props.onClick,
    className:      `scroll-view__switcher__switch switch ${props.className ? props.className : ""}`,
    imageClassName: `switch__image ${props.imageClassName ? props.imageClassName : ""}`,
    imageSrc:       `${process.env.PUBLIC_URL}/images/branding/logo-transparent.png`
  }

  return(
    <li className={data.className} switch-number={data.id} onClick={()=>{data.catchClick(data.id)}}>
      <img src={data.imageSrc} alt="Switcher" className={data.imageClassName} />
    </li>
  )
}

export default ScrollSwitch