const axios = require('axios');
const Discord = require('discord.js');
const { Intents } = require('discord.js');

const {
  Client,
  GatewayIntentBits: {
    Guilds,
    GuildMessages,
    MessageContent
  }
} = require("discord.js");
const options = {
  intents: [Guilds, GuildMessages, MessageContent],
};
const client = new Client(options);

const token = process.env.DISCORD_TOKEN;




client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}`);
});

client.on('messageCreate', message => {
  if (message.author.bot) return;
  if (message.content.includes("!db ")) {
    let str = '';
    const tar = 'html';
    const search_word = message.content.replace("!db ", "");
    const pages_num = 3;
    const apiKey = 'AIzaSyA9Af9LzT0S5A3ZzvJYfOljo4wuQPmRJ8I';
    const searchEngineId = 'a40b4c36d00694588';

    const search_word1 = search_word + ' site:battlecats-db.com/';
    const url = `https://www.googleapis.com/customsearch/v1?key=${apiKey}&cx=${searchEngineId}&q=${encodeURIComponent(search_word1)}&num=${pages_num}`;

    axios.get(url)
      .then(response => {
        const items = response.data.items;
        for (const item of items) {
          const title = item.title;
          const link = item.link;
          str += title + "\n" + link + "\n\n"
        }
        message.reply(
          {
            embeds: [{
              title: `【検索ワード】${search_word}`,
              description: str,
              color: 0xffff00

            }]
          }
        );
      })
      .catch(error => {
        console.error(error);
      });

  }
});

client.login(token);
