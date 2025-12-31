let lastIndex = 0;

// mappa fissa: 1 immagine per agente
const IMAGES = {
  "DUKE": "images/duke.png",
  "WINTHORPE": "images/winthorpe.png",
  "VALENTINE": "images/valentine.png"
};

async function pollDialogue() {
  try {
    const response = await fetch("dialogue.json?cache=" + Date.now());
    const data = await response.json();

    if (data.length > lastIndex) {
      const entry = data[lastIndex];
      showLine(entry);
      lastIndex++;
    }
  } catch (err) {
    // silenzioso: il file potrebbe non esistere ancora
  }
}

function showLine(entry) {
  document.getElementById("character-name").innerText = entry.character;
  document.getElementById("character-image").src =
    IMAGES[entry.character] || IMAGES["DUKE"];

  document.getElementById("dialogue-text").innerText = entry.text;
}

// polling ogni mezzo secondo
setInterval(pollDialogue, 500);
