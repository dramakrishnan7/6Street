import * as React from "react";
import ReactWordcloud from "react-wordcloud";

const words = [
  { text: "hello", value: 3 },
  { text: "world", value: 12.5 },
  { text: "github", value: 1 },
  { text: "code", value: 1 },
  { text: "Bob", value: 25 }
];

function WordCloud() {
  return (
    <div style={{ width: 600, height: 400 }}>
      <ReactWordcloud words={words} />
    </div>
  );
}

export default WordCloud;
