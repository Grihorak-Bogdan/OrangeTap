import ContentBlock from "../../ContentBlock/JS/ContentBlock";

import "../CSS/Content.css";

function Content(){
  return (
    <div className="content">
      <ContentBlock>
        <h1>Hello!</h1>
      </ContentBlock>
      <ContentBlock>
        <h1>Hello my friend!</h1>
      </ContentBlock>
      <ContentBlock>
        <h1>Hello my dear friend!</h1>
      </ContentBlock>
    </div>
  );
}

export default Content;