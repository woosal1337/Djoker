const Discord = require("discord.js");
const client = new Discord.Client();
const fetch = require('node-fetch');

client.login("ODI1MTQ3OTc5Njg1OTUzNTY3.YF5s8A.8TFvuA-DhNZG68cwvOZHv332CKI");

client.on("ready", () => {
    console.log("Let's Joke it up!");
});

client.on("message", msg => {

    if (msg.channel.id === "825150249797419028" || msg.channel.id === "825290843614609448") {
        if (msg.content.toLowerCase() === "djoker dark") {
            fetch('https://v2.jokeapi.dev/joke/dark', {
                method: 'GET',
            })
                .then(res => res.json())
                .then(json => {
                    if (json.type === "single") {
                        msg.channel.send(json.joke);
                    } else {
                        msg.channel.send(json.setup + "\n" + json.delivery);
                    }
                })
                .catch(err => console.log(err));
        }

        if (msg.content.toLowerCase() === "djoker programming") {
            fetch('https://v2.jokeapi.dev/joke/programming', {
                method: 'GET',
            })
                .then(res => res.json())
                .then(json => {
                    if (json.type === "single") {
                        msg.channel.send(json.joke);
                    } else {
                        msg.channel.send(json.setup + "\n" + json.delivery);
                    }
                })
                .catch(err => console.log(err));
        }

        if (msg.content.toLowerCase() === "djoker misc") {
            fetch('https://v2.jokeapi.dev/joke/misc', {
                method: 'GET',
            })
                .then(res => res.json())
                .then(json => {
                    if (json.type === "single") {
                        msg.channel.send(json.joke);
                    } else {
                        msg.channel.send(json.setup + "\n" + json.delivery);
                    }
                })
                .catch(err => console.log(err));
        }

        if (msg.content.toLowerCase() === "djoker pun") {
            fetch('https://v2.jokeapi.dev/joke/programming', {
                method: 'GET',
            })
                .then(res => res.json())
                .then(json => {
                    if (json.type === "single") {
                        msg.channel.send(json.joke);
                    } else {
                        msg.channel.send(json.setup + "\n" + json.delivery);
                    }
                })
                .catch(err => console.log(err));
        }

        if (msg.content.toLowerCase() === "djoker spooky") {
            fetch('https://v2.jokeapi.dev/joke/spooky', {
                method: 'GET',
            })
                .then(res => res.json())
                .then(json => {
                    if (json.type === "single") {
                        msg.channel.send(json.joke);
                    } else {
                        msg.channel.send(json.setup + "\n" + json.delivery);
                    }
                })
                .catch(err => console.log(err));
        }

        if (msg.content.toLowerCase() === "djoker christmas") {
            fetch('https://v2.jokeapi.dev/joke/christmas', {
                method: 'GET',
            })
                .then(res => res.json())
                .then(json => {
                    if (json.type === "single") {
                        msg.channel.send(json.joke);
                    } else {
                        msg.channel.send(json.setup + "\n" + json.delivery);
                    }
                })
                .catch(err => console.log(err));
        }
    }
})