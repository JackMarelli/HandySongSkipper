function test() {
    let rightArticleText = "Quisque nec venenatis neque. Morbi ultricies nisl lacus. Donec ipsum diam, bibendum id nulla et, ultricies volutpat metus. Maecenas sed libero vehicula, vestibulum enim ac, faucibus orci. Quisque lobortisarcu a massa placerat, quis maximus nisl auctor."
    if (document.getElementById("right-article").innerHTML = rightArticleText)
    {
        document.getElementById("right-article").innerHTML = "ma che ne so"
    }
    else
    {
        document.getElementById("right-article").innerHTML = rightArticleText
    }
}