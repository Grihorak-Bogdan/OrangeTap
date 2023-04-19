import "../CSS/ContentBlock.css";

function ContentBlock(props){
  return (
    <div className="content-block">
      <div className="content-block__container container">
        {props.children}
      </div>
    </div>
  );
}

export default ContentBlock;