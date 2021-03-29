from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Naruto_bot:
    path = "C:\Program Files (x86)\chromedriver.exe"

    def __init__(self):
        self.driver = webdriver.Chrome(self.path)

    def open_site(self):
        while True:
            try:
                self.driver.get("https://animedao.com/")
                break
            except Exception:
                time.sleep(10)
                continue

    def search_naruto(self):
        x = 0
        while x < 5:
            try:
                search = self.driver.find_element_by_xpath('/html/body/nav/div/form/div/input')
                search.send_keys("Naruto")
                break
            except Exception:
                time.sleep(10)
                self.driver.get("https://animedao.com/")
                x += 1
                continue
        time.sleep(3)
        # Select Naruto
        search_btn = self.driver.find_element_by_xpath('/html/body/nav/div/form/div/span/button/span')
        search_btn.click()
        time.sleep(2)

    def open_episode(self):
        print("Title: " + self.driver.title)  # show the title of the browser page
        naruto_series = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/a/div/div/div[1]/center/img')
        naruto_series.click()
        fr = open("episodes.txt", "r")  # Open episodes text to read what episode I will watch
        episode = fr.read()  # read the episode I'm on
        prev_episode = episode  # set the episode to change for the next episode
        fr.close()  # Close
        time.sleep(2)
        naruto_episode = self.driver.find_element_by_xpath('//*[@id="eps"]/div/a[' + episode + ']/div/div/div/div')
        naruto_episode.click()

        time.sleep(5)
        fr.close()

        fw = open("episodes.txt", "w")  # Open episodes text to change to the next episode
        next_episode = int(prev_episode) + 1  # add 1 so I will watch the next episode when I press this
        fw.write(str(next_episode))  # write into the text
        fw.close()  # Close the text

    def choice(self):
        while True:
            inp = int(input("What would you like to do?"
                            "\n 1) Next episode"
                            "\n 2) Stop process"))

            if inp == 1:
                self.next_episode_updated()
            if inp == 2:
                self.driver.quit()
                break
            else:
                print("Invalid input!")

    def next_episode_updated(self):
        self.driver.get("https://animedao.com/anime/naruto/")
        fr = open("episodes.txt", "r")  # Open episodes text to read what episode I will watch
        episode = fr.read()  # read the episode I'm on
        prev_episode = episode  # set the episode to change for the next episode
        fr.close()  # Close
        time.sleep(2)

        while True:
            try:
                naruto_episode = self.driver.find_element_by_xpath('//*[@id="eps"]/div/a[' + episode + ']/div/div/div/div')
                time.sleep(2)
                naruto_episode.click()
                break
            except Exception:
                time.sleep(5)
                continue

        time.sleep(5)
        fr.close()

        fw = open("episodes.txt", "w")  # Open episodes text to change to the next episode
        next_episode = int(prev_episode) + 1  # add 1 so I will watch the next episode when I press this
        fw.write(str(next_episode))  # write into the text
        fw.close()  # Close the text

        # print("You have just watched episode "+episode+", next click is going to be "+str(next_episode))
        # print("WARNING! closing this will kill the process and close the browser!")
        # print("Option 2 DOES NOT WORK YET!")

    def prev_episode(self):  ## does not properly work yet!
        prev_ = self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/center[1]/div/a[1]/button/span")
        prev_.click()
        print("You're watching episode" + episode)

# print("You have just watched episode "+episode+", next click is going to be "+str(next_episode))
# print("WARNING! closing this will kill the process and close the browser!")
# print("Option 2 DOES NOT WORK YET!")


# def nxt_episode():
#     next_ = self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/center[1]/div/a[3]/button/span")
#     next_.click()
#
#     fr = open("episodes.txt", "r")  # Open episodes text to read what episode I will watch
#     episode = fr.read()  # read the episode I'm on
#     prev_episode = episode  # set the episode to change for the next episode
#     fr.close()  # Close
#     fw = open("episodes.txt", "w")  # Open episodes text to change to the next episode
#     next_episode = int(prev_episode) + 1  # add 1 so I will watch the next episode when I press this
#     fw.write(str(next_episode))  # write into the text
#     fw.close()  # Close the text


bot = Naruto_bot()
bot.open_site()
bot.search_naruto()
bot.open_episode()
bot.choice()


# while True:
#     choice = int(input("Press 1 for next episode, 3 for exit"))
#     if choice == 1:
#         bot = Naruto_bot()
#     #if choice == 2:
#     #   prv_episode()
#     if choice == 3:
#         print("Thank you for using this code")
#         time.sleep(3)
#         driver.quit()
#         break
#



