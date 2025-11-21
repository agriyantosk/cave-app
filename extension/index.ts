interface Character {
  name: string;
  house: string;
  playsQuidditch: boolean;
  position: string;
  quidditchYears: number[];
}

const response = fetch(
  "https://coderbyte.com/api/challenges/json/quidditch-list"
)
  .then((result) => result.json())
  .then((jsonformat) => console.log(jsonformat));

const characters: Character[] = [];
const result = [];
for (let index = 0; index < characters.length; index++) {
  const element = characters[index];
  let temp = "";
  temp + element.name + " " + element.house;
  console.log(temp);
  result.push(temp);
  temp = "";
}
