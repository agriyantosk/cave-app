import { useEffect } from "react";
import "./Popup.css";
import { Toggle } from "../components/Toggle";
import "../popup.css";

export default function () {
  useEffect(() => {
    console.log("Hello from the popup!");
  }, []);

  return (
    <>
      <div>
        <img src="/icon-with-shadow.svg" />
        <h1 className="text-blue-400 italic">vite-plugin-web-extension</h1>
        <p>
          Template: <code className="text-white">ANJEEENGGG</code>
        </p>
        <div>
          <Toggle /> <span className="text-white">this is toggle</span>
        </div>
      </div>
    </>
  );
}
