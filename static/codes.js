const links = {
    "Brazil": "https://www.google.ca/maps/place/Brazil/@-13.6561589,-69.7309264,4z/data=!3m1!4b1!4m5!3m4!1s0x9c59c7ebcc28cf:0x295a1506f2293e63!8m2!3d-14.235004!4d-51.92528",
    "China": "https://www.google.ca/maps/place/China/@34.4453421,86.0120883,4z/data=!3m1!4b1!4m5!3m4!1s0x31508e64e5c642c1:0x951daa7c349f366f!8m2!3d35.86166!4d104.195397",
    "Canada": "https://www.google.ca/maps/place/Canada/@50.8469872,-130.2334674,3z/data=!3m1!4b1!4m5!3m4!1s0x4b0d03d337cc6ad9:0x9968b72aa2438fa5!8m2!3d56.130366!4d-106.346771",
    "Thailand": "https://www.google.ca/maps/place/Thailand/@12.9036593,92.4368173,5z/data=!3m1!4b1!4m5!3m4!1s0x304d8df747424db1:0x9ed72c880757e802!8m2!3d15.870032!4d100.992541",
    "UK": "https://www.google.ca/maps/place/United+Kingdom/@54.2308315,-13.4380293,5z/data=!3m1!4b1!4m5!3m4!1s0x25a3b1142c791a9:0xc4f8a0433288257a!8m2!3d55.378051!4d-3.435973"
};

const flags = {
    "Brazil": "https://img.theculturetrip.com/768x432/wp-content/uploads/2017/06/brazili-flaf.png",
    "China": "https://cdn.britannica.com/90/7490-004-415899A0/Flag-China.jpg",
    "Canada": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Flag_of_Canada_%28Pantone%29.svg",
    "Thailand": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Flag_of_Thailand.svg",
    "UK": "https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/1200px-Flag_of_the_United_Kingdom.svg.png"
};

const formats = {
    "Brazil": "NNNNNNNN",
    "China": "NNNNNN",
    "Canada": "ANA NAN",
    "Thailand": "NNNNN",
    "UK": "AANNAA / AANANAA / AANNNAA / ANNAA / ANANAA / ANNNAA"
};

const regexp = {
    "Brazil": /^\d{8}$/,
    "China": /^\d{6}$/,
    "Canada": /^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$/,
    "Thailand": /^\d{5}$/,
    "UK": /(^[A-Za-z]{2}\d{2}[A-Za-z]{2}$)|(^[A-Za-z]{2}\d[A-Za-z]\d[A-Za-z]{2}$)|(^[A-Za-z]{2}\d{3}[A-Za-z]{2}$)|(^[A-Za-z]\d{2}[A-Za-z]{2}$)|(^[A-Za-z]\d[A-Za-z]\d[A-Za-z]{2}$)|(^[A-Za-z]\d{3}[A-Za-z]{2}$)/
};

function updateCountry() {
            selectElement = document.querySelector('#select1');
            country = selectElement.options[selectElement.selectedIndex].value;
            document.getElementById("image").src = flags[country];
            document.getElementById("link").href = links[country];
            document.getElementById("postal").innerHTML = formats[country];
            validate_code();
}

function validate_code() {
    country = selectElement.options[selectElement.selectedIndex].value;
    const code_re
       = regexp[country];
     const code_input = document.getElementById("code");

     code_input.value = code_input.value.trim();

     if (code_re.test(code_input.value)) {
        code_input.className = "";
    } else {
        code_input.className = "error";
        // phone_input.classList.add("error");
        code_input.className += " error_big";
        // phone_input.classList.add("error_big");
    }
};